[Implemations and changes](#implemations-and-changes)

ENV File Parameters

Put it next to the app

```
EXTERNAL_FASTAPI_PORT = 80
INTERNAL_FASTAPI_PORT = 8000

MONGO_HOST=mongo-db
MONGO_PORT=27017
MONGO_INITDB_ROOT_USERNAME=root
MONGO_INITDB_ROOT_PASSWORD=rootpassword
MONGO_INITDB_DATABASE=db

JWT_SECRET = uDQs2sC8L6LDufZMdAdyhpge1rZPrj0XhYyxBBg8hCs=
JWT_ALGORITHM = HS256
JWT_EXPIRATION_MINUTES = 10

DEFAULT_PAGE_SIZE = 3
```

To Run

```
fastapi dev app/src/main.py
```

To run unit tests:

```
python -m app.src.tests.unit.run_tests
```

## App architecture description

### Infra Layer

In this layer, the application infrastructure is defined, such as:

- Authentication utilities such as token creation, management, and validation

- Database client and its models (tables)

- Errors related to this layer and other layers

  - include status code and message

- Services for interacting with external APIs

  - include interfaces and their implementation

- Fastapi config such as

  - middleware
  - tasks that should be run on startup or shutdown, such as create and close database client
  - implement some states based on settings loaded from .env in main app, to have access them throughout the entire project

- Mixin classes

- Application settings load from the `.env` file
  - load with pydantic_settings

```
infra/
│
├── auth/
│   └── <files or directories...>
│
├── db/
│   ├── redis/
│   │   └── <files or directories...>
│   │
│   ├── mongodb/
│   │   └── <files or directories...>
│   │
│   └── sqlite/
│       └── <files or directories...>
│
├── exceptions/
│   └── <files...>
│
├── external_api/
│   ├── interface/
│   │   └── <files...>
│   │
│   └── service/
│       └── <files...>
│
├── fastapi_config/
│   └── <files...>
│
├── mixins/
│   └── <files...>
│
└── settings/
    └── <files...>
```

### Domain Layer

In this layer, data models are defined that are only used inside the application, meaning between layers, for transferring data.

```
domain/
├── mock_data/
│   └── <files...>
│
└── schemas/
    └── <schema_group_name>/
       └── <files...>
```

### Models Layer

In this layer, data models are defined that are only used for receiving or sending data to the client.

```
models/
├── filter/
│   └── <files...>
│
└── schemas/
    └── <schema_group_name>/
        └── <files...>

```

### Repo Layer

In this layer, communication with the database is handled.
Repository classes are defined here, whose methods provide interaction with the database.
Each repository class inherits from an interface defined in this layer.
Interfaces define the structure of database communication, so we can have multiple repository classes based on a single interface and use them for dependency injection.

```
repo/
├── interface/
│   └── <files...>
│
└── <implementation_name>/
    └── <files...>
```

Naming implementations can be based on:

- **Storage type** — for example: `sql`, `nosql`

```
repo/
├── interface/
│   └── <files...>
│
├── sql/
│   └── <files...>
│
└── nosql/
    └── <files...>
```

- **Storage name** — for example: `postgresql`, or `mongodb`.

```
repo/
├── interface/
│   └── <files...>
│
├── postgresql/
│   └── <files...>
│
└── mongodb/
    └── <files...>
```

### Routes Layer

In this layer, endpoints are defined along with their dependencies, response statuses, and other endpoint-related configurations.

```
routes/
├── api_endpoints/
│   ├── <endpoint_group_name>/
│   │   └── <files...>
│   │
│   ├── <endpoint_group_name>/
│   │   └── <files...>
│   │
│   └── main_router.py
│
├── depends/
│   └── <files...>
│
└── http_response/
    └── <files...>
```

### Usecase Layer

In this layer, the application’s business logic is defined.
This layer acts as an important bridge between endpoints in the Routes layer, the database in the Repo layer, and external APIs in the Infra layer.

```
usecase/
├── <usecase_group_name>/
│   └── <files...>
│
└── <usecase_group_name>/
    └── <files...>
```

#### Note

The layers are not limited to the mentioned items and can also include other related configurations.

## Implemations and changes

The items in the file **d_1.py**, except for `get_status_list_from_query`, included token generation and authentication services.
The environment variables in the file were all moved to **.env** and are loaded through the **Setting** pydantic class in `app.src.infra.settings.settings`.

For token management and validation, the **JWTHandler** pydantic class is defined in `app.src.infra.auth.jwt_handler`.
The functions `create_jwt_token` and `verify_token`, which previously did not exist in this file and the application, are now defined in this class.
Additionally, the `decode_token` function has been rewritten.

The items included in the payload are defined in the **JWTPayload** pydantic class located in `app.src.domain.schema.auth.jwt_payload`.

Since we defined `user_type` directly in the payload, the functions `check_user_is_admin` and `get_email_from_token` were no longer needed and were removed.
The `user_type` check is now implemented as a dependency in `app.src.routs.depend.auth.depend`.

The function `get_status_list_from_query` was also unrelated in this file, and because we use a **Pydantic model class** to receive data from the header, which automatically handles what this function did, it was removed.

---

In the file **d_2.py**, we also had database-related environment variables, which were moved to **.env** as well.
Additionally, the database client and its collections were moved to
`app.src.infra.db.mongodb.client.py` and `app.src.infra.db.mongodb.collections/`.

The collections were defined based on the pydantic class models in `app.src.domain.schemas` and inherit from them.

---

In the **main.py** file, all the inputs of the defined endpoint are specified as parameters of the **PayoutFilter** class in `app.src.models.filter.payout_filter.py`.

---

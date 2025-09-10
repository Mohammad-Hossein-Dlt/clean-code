ENV File Parameters

Put it next to the src

```
MONGO_HOST=mongo-db
MONGODB_PORT=27017
MONGO_INITDB_ROOT_USERNAME=root
MONGO_INITDB_ROOT_PASSWORD=rootpassword
MONGO_INITDB_DATABASE=db

JWT_SECRET = secret
JWT_ALGORITHM = HS256
JWT_EXPIRATION_MINUTES = 10

DEFAULT_PAGE_SIZE = 3
```

To Run

```
fastapi dev .\src\main.py
```

## App architecture description

### Infra Layer

In this layer, the application infrastructure is defined, such as:

- Fastapi config such as
  - middleware
  - tasks that should be run on startup or shutdown,
  - implement some states based on settings loaded from .env in main app to have access them throughout the entire project
- Application settings load from the `.env` file
  - load with pydantic_settings
- Services for interacting with external APIs
  - include interfaces and their implementation
- Errors related to this layer and other layers
  - include status code and message
- Database and its models (tables)
- Mixin classes

```
infra/
├── db/
│   ├── redis/
│   │   └── <files or directories...>
│   │
│   └── service/
│       └── <files or directories...>
│
├── exception/
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
└── schemas/
    ├── <schema_group_name>/
    │   └── <files...>
    │
    ├── <schema_group_name>/
    │   └── <files...>
    │
    └── <schema_group_name>/
        └── <files...>
```

### Models Layer

In this layer, data models are defined that are only used for receiving or sending data to the client.

```
models/
└── schemas/
    ├── <schema_group_name>/
    │   └── <files...>
    │
    ├── <schema_group_name>/
    │   └── <files...>
    │
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
└── <implementation_name>/
    └── <files...>
```

Naming implementations can be based on:

- **Storage type** — for example: `sql`, `nosql`

```
repo/
├── interface/
│   └── <files...>
├── sql/
│   └── <files...>
└── nosql/
    └── <files...>
```

- **Storage name** — for example: `postgresql`, or `mongodb`.

```
repo/
├── interface/
│   └── <files...>
├── postgresql/
│   └── <files...>
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

One of the implementen logics is the token refresh mechanism.

```
usecase/
├── <usecase_group_name>/
│   └── <files...>
│
├── <usecase_group_name>/
│   └── <files...>
│
└── <usecase_group_name>/
    └── <files...>
```

#### Note

The layers are not limited to the mentioned items and can also include other related configurations.

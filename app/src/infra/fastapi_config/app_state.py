from enum import Enum
from fastapi import FastAPI
from typing import Any

class AppStates(str, Enum):
    JWT_SECRET = "auth_base_url"
    JWT_ALGORITHM = "auth_db_client"
    JWT_EXPIRATION_MINUTES = "jwt_expiration_minutes"
    DEFAULT_PAGE_SIZE = "default_page_size"

def set_app_state(app: FastAPI, key, value: Any):
    """Set a state in the FastAPI app."""
    app.state.__setattr__(key, value)


def get_app_state(app: FastAPI, key):
    """Get a state from the FastAPI app."""
    return app.state.__getattr__(key)

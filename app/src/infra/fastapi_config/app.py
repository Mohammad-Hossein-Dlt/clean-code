from fastapi import FastAPI
from fastapi_swagger import patch_fastapi
from .app_lifespan import lifespan

app: FastAPI = FastAPI(
    root_path="/artist-service",
    lifespan=lifespan,
    docs_url=None,
    swagger_ui_oauth2_redirect_url=None,
) 

patch_fastapi(app, docs_url="")
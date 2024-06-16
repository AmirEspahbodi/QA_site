from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from apis import root_api_router
from core.config.app import AppConfig
from core.utils import logging_middleware
from ai.q_a import qa


def init_routers(app_: FastAPI) -> None:
    app_.include_router(root_api_router)


def init_logger(app_: FastAPI) -> None:
    app_.middleware("http")(logging_middleware)


def init_cors(app_: FastAPI) -> None:
    app_.add_middleware(
        CORSMiddleware,
        allow_origins=AppConfig.ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )




@asynccontextmanager
async def lifespan(app: FastAPI):
    app.qa_ml_model = qa
    yield
    app.qa_ml_model = None


def create_app() -> FastAPI:
    # init app
    _app = FastAPI(
        title=AppConfig.APP_NAME,
        description=AppConfig.APP_DESCRIPTION,
        version=AppConfig.APP_VERSION,
        docs_url=None if AppConfig.ENVIRONMENT == "production" else "/docs",
        redoc_url=None,
        lifespan=lifespan
    )
    init_cors(app_=_app)
    init_logger(app_=_app)
    init_routers(app_=_app)

    return _app


app = create_app()

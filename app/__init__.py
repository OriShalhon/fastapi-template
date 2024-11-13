import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1 import router as api_router
from app.core.config import configure_logging, load_configurations


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup event
    logging.info("Application startup")

    yield

    logging.info("Application shutdown")


def create_app() -> FastAPI:
    app = FastAPI()

    load_configurations(app)
    configure_logging()

    app.include_router(api_router)
    app.router.lifespan_context = lifespan
    return app

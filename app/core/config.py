import logging
import os
from logging.handlers import RotatingFileHandler

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def load_configurations(app: FastAPI) -> None:
    # Enable CORS - Cross-Origin Resource Sharing currently allows all origins
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"], # edit this to allow only specific origins 
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def configure_logging(log_dir: str = None, log_level=logging.INFO) -> None:
    if log_dir is None:
        log_dir = (
            os.getcwd()
        )  # Use current directory if no custom log directory is provided

    log_file = os.path.join(log_dir, "app.log")

    # Set up rotating file handler to limit file size to 5 MB with up to 5 backup files
    file_handler = RotatingFileHandler(
        log_file, maxBytes=5 * 1024 * 1024, backupCount=5
    )

    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[file_handler, logging.StreamHandler()],
    )

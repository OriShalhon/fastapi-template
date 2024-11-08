import logging
import uvicorn

from app.models import models
from app.db.database import engine
from app import create_app

app = create_app()

models.Base.metadata.create_all(bind=engine)

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logging.info("Starting the application")
    logging.info(f"app.state: {app.state}")

    uvicorn.run(app, host="0.0.0.0", port=8000)

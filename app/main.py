import logging

import uvicorn

from app import create_app

# from app.db.database import engine
# from app.models import models

app = create_app()

# with alembic this is not needed, choose one of the two
# models.Base.metadata.create_all(bind=engine)

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logging.info("Starting the application")
    logging.info(f"app.state: {app.state}")

    uvicorn.run(app, host="0.0.0.0", port=8000)

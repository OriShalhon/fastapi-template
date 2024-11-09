# FastAPI PostgreSQL Boilerplate

This project serves as a starting template for creating **FastAPI** applications with **PostgreSQL** as the database, **SQLAlchemy** as the ORM, **Ruff** for linting, and **GitHub Actions** configured for automated linting and testing. 


> **Note**: This project is a work in progress. Not all features described in this README are fully implemented yet.

## Features

- **FastAPI**: High-performance API framework.
- **PostgreSQL**: Robust, scalable SQL database.
- **SQLAlchemy**: ORM for database interactions.
- **Ruff**: Fast and flexible Python linter.
- **GitHub Actions**: CI/CD pipeline for linting and testing.

## Project Structure

```plaintext
.
├── app
│   ├── api             # API route definitions
│   ├── core            # Configuration and core settings
│   ├── db              # Database setup and session management
│   ├── models          # SQLAlchemy models
│   ├── schemas         # Pydantic schemas for request and response models
│   ├── services        # Business logic and service layer
│   ├── main.py         # Application entry point
│   └── tests           # Unit and integration tests
├── .github
│   └── workflows       # GitHub Actions for linting and testing
├── .env.example        # Example environment variables
├── Dockerfile          # Docker configuration
├── requirements.txt    # Python dependencies
├── ruff.toml           # Ruff linting configuration
└── README.md           # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/username/fastapi-postgresql-boilerplate.git
   cd fastapi-postgresql-boilerplate
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   Copy the `.env.example` file to `.env` and update the values according to your environment.

5. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

6. Access the API documentation at `http://127.0.0.1:8000/docs`.

### Database Migration (Alembic)

To set up database migrations with Alembic:

```bash
alembic init migrations
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

## Linting

Run Ruff to check for code quality issues:
```bash
ruff check .
```

## Testing

To run the tests:

```bash
pytest
```

## Continuous Integration

GitHub Actions is configured to run linting and tests automatically on push or pull requests.

- **Linting**: Checks for code quality using Ruff.
- **Testing**: Runs all unit and integration tests.

## Contributing

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.
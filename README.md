## OVERVIEW
Task Management API

An async REST API for task management, built with FastAPI and PostgreSQL.

Current Status

Version: v0.2.0

The project currently contains the backend foundation:

FastAPI application

Async Python endpoints

Environment-based configuration with Pydantic Settings

SQLAlchemy 2.x async database layer

asyncpg PostgreSQL driver

Async SQLAlchemy sessions

PostgreSQL connectivity health check

Git-based versioning

Tech Stack

Python 3.12+

FastAPI

Pydantic v2

Pydantic Settings

SQLAlchemy 2.x

PostgreSQL

asyncpg

Alembic

pytest

Ruff

Project Structure
app/
├── core/
│   └── config.py
├── db/
│   ├── base.py
│   └── session.py
└── main.py

tests/

.env.example
.gitignore
pyproject.toml

Running Locally

Create and activate a virtual environment:

python3 -m venv .venv
source .venv/bin/activate


Install the project and development dependencies:

pip install -e ".[dev]"


Create a .env file based on .env.example and configure the PostgreSQL connection.

Start the development server:

uvicorn app.main:app --reload


The API will be available at:

http://127.0.0.1:8000


Interactive API documentation:

http://127.0.0.1:8000/docs

Health Checks

Application health:

GET /health


Database connectivity:

GET /health/db


The database health endpoint verifies that the application can communicate with PostgreSQL through SQLAlchemy's asynchronous engine.

Roadmap

 FastAPI project foundation

 Async application setup

 PostgreSQL connectivity

 SQLAlchemy async database layer

 Alembic migrations

 Task database model

 Task CRUD endpoints

 Validation and error handling

 Authentication and authorization

 Automated tests

 Production configuration

 Containerization and deployment

Versioning

The project uses Git tags for milestone versions.

Current milestone: continuous deployment

v0.2.0


Future versions will represent meaningful increments in the API's development.

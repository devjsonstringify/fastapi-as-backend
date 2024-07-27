# FastAPI CRUD Application

This is a basic FastAPI project that demonstrates how to build a CRUD (Create, Read, Update, Delete) application with database integration.

## Features

- **Create**: Add new records to the database.
- **Read**: Retrieve and display records from the database.
- **Update**: Modify existing records in the database.
- **Delete**: Remove records from the database.

## Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.6+.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **SQLite**: Lightweight database used for this example (can be replaced with other databases).

## Installation

1. **Clone the repository**:

    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

The project uses SQLite by default. If you want to use a different database, you can configure the `DATABASE_URL` in `config.py` or `main.py`.

## Running the Application

To start the FastAPI server with automatic reloading, run:

```bash
uvicorn main:app --reload

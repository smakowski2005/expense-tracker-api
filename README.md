# Expense Tracker API

A RESTful API for managing personal expenses, built with Python and FastAPI. The application supports user registration, JWT authentication, and CRUD operations for expenses. Each user can access and manage only their own expenses.

## Features

- User registration with password hashing
- User authentication using JSON Web Tokens (JWT)
- Create, retrieve, update, and delete expenses
- Associate each expense with its owner
- Filter expenses by name and category
- Paginate expense results
- Validate request data using Pydantic
- Store data in an SQLite database using SQLAlchemy
- Automated tests using pytest

## Tech Stack

- **Python**
- **FastAPI** — API framework
- **SQLAlchemy** — ORM and database operations
- **SQLite** — database
- **Pydantic** — data validation
- **JWT** — authentication
- **Passlib and bcrypt** — password hashing
- **pytest and HTTPX** — testing

## Project Structure

```text
expense-tracker-api/
├── app/
│   ├── routes/
│   │   ├── expenses.py
│   │   └── users.py
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── security.py
├── tests/
│   ├── __init__.py
│   └── test_user.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone <https://github.com/smakowski2005/>
cd expense-tracker-api
```


### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and configure the environment variables required by the application.

Never commit your real `.env` file or secret keys to version control. Use `.env.example` to document the required variables without exposing real credentials.

### 5. Run the application

```bash
uvicorn app.main:app --reload
```

Once the server is running, open `/docs` on the local server to explore the interactive Swagger UI and test the API endpoints.

## API Endpoints

### Authentication and Users

| Method | Endpoint | Description |
|---|---|---|
| POST | `/users/` | Register a new user |
| POST | `/token` | Authenticate a user and obtain a JWT access token |

### Expenses

The expense endpoints require authentication. Include a valid access token when making requests.

| Method | Endpoint | Description |
|---|---|---|
| POST | `/expenses/` | Create an expense |
| GET | `/expenses/` | Retrieve expenses, with pagination and filtering |
| GET | `/expenses/{expense_id}` | Retrieve a specific expense |
| PUT | `/expenses/{expense_id}` | Update an expense |
| DELETE | `/expenses/{expense_id}` | Delete an expense |

The API enforces ownership: users can access and modify only expenses associated with their own accounts.

For exact request fields, response formats, and available query parameters, refer to the interactive API documentation at `/docs`.

## Running Tests

Run
# Trivia Quiz Backend API

This is a simple backend API for a Trivia Quiz application.
It allows creating and retrieving questions with multiple choices.

Key Features:
- Implements RESTful API usisng FastAPI
- **PostgreSQL** to store quiz data
- **pgAdmin** for database management
- Databse integration using **SQLAlchemy** ORM
- Dependency management with **Poetry**
- Data validation with **Pydantic** models


## Setup

Clone the repo
```
git clone https://github.com/khadija-ahmadova/fastapi-postgresql-app
cd fastapi-postgresql-app
```

Install dependencies
```
poetry install
```

Save database url as environment variable
```
DATABASE_URL=postgresql://postgres:password@localhost:5432/dbname
```

Run the app
```
poetry run uvicorn main:app --reload
```

Navigate to API docs `http://127.0.0.1:8000/docs` to try out endpoints

Example Request Payload for POST /questions/ endpoint
```
{
  "question_text": "What is the capital of France?",
  "choices": [
    {"choice_text": "Paris", "is_correct": true},
    {"choice_text": "London", "is_correct": false},
    {"choice_text": "Berlin", "is_correct": false}
  ]
}
```


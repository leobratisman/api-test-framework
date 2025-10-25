# API to automate by tests

## Install Poetry

```shell
curl -sSL https://install.python-poetry.org | python3 -
```

## Install requirements

```shell
poetry install --no-root
```

## Create `.env` file

To get started with the project, you need to create a `.env` file in the root of the project directory. This file will
store sensitive environment variables such as database credentials, JWT settings and test framework's settings.

### Step-by-Step Guide:

#### 1. Create a .env File:

In your project root directory, create a file named .env.

```shell
touch .env
```

#### 2. Add the Required Variables:

Copy and paste the following environment variables into the `.env` file:

```shell
APP_HOST="http://localhost:8000"

DATABASE_URL="sqlite+aiosqlite:///./local.db"

JWT_ALGORITHM="HS256"
JWT_SECRET_KEY="some_your_secret_key"
JWT_ACCESS_TOKEN_EXPIRE=1800
JWT_REFRESH_TOKEN_EXPIRE=5184000

API_BASE_URL=http://127.0.0.1:8000/api/v1
API_AUTH_URL=http://127.0.0.1:8000/api/v1/authentication
TIMEOUT=2

TEST_DATA_DIR=./qa/static/
```

## Run server

```shell
uvicorn main:app --reload
```

## Run API-tests

```shell
poetry run pytest qa
```

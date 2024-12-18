# FastAPI + PostgreSQL

Installation Steps for FastAPI Invsmart project.

### Step 1: Clone the Repository

```bash
git https://github.com/pratham1659/backend-invsmart.git
```

### Step 2: Steps to Create and Use a Poetry Virtual Environment

```bash
poetry init
poetry install
poetry shell
```

### Step 4: Check the Virtual Environment Path

```bash
poetry env info
```

### Step 5: Run the application

```bash
uvicorn app.main:app --reload
```

Also run it like by making some modification in toml files and main file

```bash
poetry run start
```

### Step 6: create a `.env` file for sensitive variables

in FastAPI

```bash
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env file

DB_URL = DB_URL=postgresql+asyncpg://username:password@localhost/dbname


DATABASE_URL = os.getenv("DB_URL")
API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
```

### Step 7: Deactivate the Virtual Environment

When you're done working in the Poetry shell, deactivate it with:

```bash
exit
```

## step 8: Configure Poetry to Always Create Virtual Environments in the Project Folder

By default, Poetry creates virtual environments outside your project directory. To store the virtual environment in the project folder:

```bash
poetry config virtualenvs.in-project true
poetry install
```

## step 9: Important keys that we have used in this projects

The command produces 32 random bytes in hexadecimal format, which results in a string with 64 characters (since each byte is represented by two hex characters).

```bash
openssl rand -hex 32
```

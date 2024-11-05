# FastAPI + PostgreSQL

# Installation Steps for My Project

## Step 1: Clone the Repository

```bash
git https://github.com/pratham1659/backend-invsmart.git
```

# Step 2: Create and activate a virtual environment

```bash
python -m venv venv
```

```bash
source venv/bin/activate (Linux/Mac)
```

```bash
venv\Scripts\activate (Windows)
```

# Step 4: Install dependencies

```bash
pip install -r requirements.txt
```

# Step 5: Run the application

````bash
uvicorn main:app --reload
```bash
````

# Step 6: create a `.env` file for sensitive variables

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

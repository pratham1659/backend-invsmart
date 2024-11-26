import uvicorn
from fastapi import FastAPI, Header
from app.router.routes import book_router
import os
from dotenv import load_dotenv
from datetime import datetime
from contextlib import asynccontextmanager
from app.config.dbconfig import init_db

load_dotenv()


@asynccontextmanager
async def life_span(app: FastAPI):
    print(f"🚀 [STARTUP] FastAPI server is warming up. Time: {
          datetime.now()} 🚀")
    await init_db()
    yield
    print(f"🛑 [SHUTDOWN] FastAPI server is winding down. Time: {
          datetime.now()} 🛑")

version = os.getenv("VERSION")


def init_app():
    app = FastAPI(
        title="Inventory Insight App",
        description="Login Page",
        version=version,
        lifespan=life_span
    )
    return app


app = init_app()


@book_router.get("/")
async def root():
    return {"message": "Welcomt to FastAPI"}


@book_router.get("/get_headers", status_code=201)
async def get_header(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None)

):
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-Agent"] = user_agent
    request_headers["Host"] = host

    return request_headers


app.include_router(book_router, prefix="/api/{version}/books", tags=['books'])


def start():
    """Launched with 'poetry run start' at root level """
    uvicorn.run("app.main:app", host="localhost", port=8888, reload=True)

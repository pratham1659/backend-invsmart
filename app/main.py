import uvicorn
from datetime import datetime
from fastapi import FastAPI, Header
from contextlib import asynccontextmanager
from app.config.dbconfig import init_db
from app.router.book_routes import book_router
from app.router.auth_routes import auth_router
from app.config.settings import Config

# Lifecycle Management


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"🚀 [STARTUP] FastAPI server is warming up. Time: {
          datetime.now()} 🚀")
    await init_db()
    yield
    print(f"🛑 [SHUTDOWN] FastAPI server is winding down. Time: {
          datetime.now()} 🛑")


# Application Factory


def create_app() -> FastAPI:
    app = FastAPI(
        title="Inventory Insight App",
        description="Login Page",
        version=Config.VERSION,
        lifespan=lifespan,
    )

    # Include Routers
    app.include_router(
        book_router, prefix=f"/api/{Config.VERSION}/books", tags=["books"]
    )
    app.include_router(
        auth_router, prefix=f"/api/{Config.VERSION}/auth", tags=["auth"])

    # Add Routes
    app.add_api_route("/", root, methods=["GET"], tags=["General"])
    app.add_api_route(
        "/get_headers", get_headers, methods=["GET"], status_code=201, tags=["General"]
    )

    return app


# Routes


async def root():
    return {"message": "Welcome to FastAPI"}


async def get_headers(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None),
):
    return {
        "Accept": accept,
        "Content-Type": content_type,
        "User-Agent": user_agent,
        "Host": host,
    }


# Initialize Application
app = create_app()

# Entry Point


def start():
    """Launched with 'poetry run start' at root level."""
    uvicorn.run("app.main:app", host="localhost", port=8888, reload=True)

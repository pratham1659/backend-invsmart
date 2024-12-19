import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.dbconfig import init_db
from app.config.redis_connect import connect_to_redis
from app.books.book_routes import book_router
from app.auth.auth_routes import auth_router
from app.reviews.review_routes import review_router
from app.tags.tags_routes import tags_router
from app.config.settings import Config
from app.config.errors import register_all_errors
from app.config.middleware import register_middleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 [STARTUP] FastAPI server is warming up. Time: 🚀")
    await init_db()
    await connect_to_redis()
    yield
    print("🛑 [SHUTDOWN] FastAPI server is winding down. Time: 🛑")


description = """
A REST API for a book review web service.

This REST API is able to;
- Create Read Update And delete books
- Add reviews to books
- Add tags to Books e.t.c.
    """

version_prefix = f"/api/{Config.VERSION}"
app = FastAPI(
    title="Bookly",
    description=description,
    version=Config.VERSION,
    # lifespan=lifespan,
    license_info={"name": "MIT License",
                  "url": "https://opensource.org/license/mit"},
    contact={
        "name": "Ssali Jonathan",
        "url": "https://github.com/jod35",
        "email": "ssalijonathank@gmail.com",
    },
    terms_of_service="httpS://example.com/tos",
    openapi_url=f"{version_prefix}/openapi.json",
    docs_url=f"{version_prefix}/docs",
    redoc_url=f"{version_prefix}/redoc"
)


register_all_errors(app)
register_middleware(app)

# Include Routers
app.include_router(
    book_router, prefix=f"/api/{Config.VERSION}/books", tags=["books"]
)
app.include_router(
    auth_router, prefix=f"/api/{Config.VERSION}/auth", tags=["auth"])
app.include_router(
    review_router, prefix=f"/api/{Config.VERSION}/reviews", tags=["reviews"]
)
app.include_router(
    tags_router, prefix=f"/api/{Config.VERSION}/tags", tags=["tags"])


def start():
    """Launched with 'poetry run start' at root level."""
    uvicorn.run("app.main:app", host="localhost", port=8888, reload=True)

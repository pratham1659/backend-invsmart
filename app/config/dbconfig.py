from sqlmodel import create_engine, SQLModel
from sqlalchemy.ext. asyncio import AsyncEngine
from app.config.dbsettings import Config
from app.model.bookmodel import Book

engine = AsyncEngine(
    create_engine(
        url=Config.DATABASE_URL,
        echo=True
    ))


async def init_db():
    async with engine.begin() as conn:
        """Initialize the database by creating all tables defined in the models."""
    async with engine.begin() as conn:
        # Use run_sync to create all tables defined in SQLModel's metadata
        await conn.run_sync(SQLModel.metadata.create_all)

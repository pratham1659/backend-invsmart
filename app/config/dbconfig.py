
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from app.config.logger import setup_logger

# Set up logger
logger = setup_logger(__name__)

# Retrieve the database URL
DATABASE_URL = "postgresql+asyncpg://postgres:mysql@localhost:5432/test"
if not DATABASE_URL:
    logger.error("DATABASE_URL is not set in the environment variables.")
    raise ValueError("DATABASE_URL is not set in the environment variables.")


class AsyncDatabaseSessions:
    def __init__(self) -> None:
        self.session = None
        self.engine = None

    def __getattr__(self, name):
        # Return an attribute from the session
        return getattr(self.session, name)

    def init(self):
        """Initialize the database engine and session."""
        try:
            self.engine = create_async_engine(DATABASE_URL, echo=True)
            logger.info("Database engine created successfully.")
            # Session creation, but no active session yet
            self.session = sessionmaker(
                self.engine, expire_on_commit=False, class_=AsyncSession)()
        except Exception as e:
            logger.error(f"Error initializing database connection: {e}")
            raise

    async def create_all(self):
        """Create all tables in the database."""
        try:
            async with self.engine.begin() as conn:
                await conn.run_sync(SQLModel.metadata.create_all)
            logger.info(
                "Database tables created successfully (if they didn't exist).")
        except Exception as e:
            logger.error(f"Error creating tables: {e}")
            raise

    async def close(self):
        """Close the session."""
        try:
            if self.session:
                await self.session.close()
                logger.info("Database session closed successfully.")
        except Exception as e:
            logger.error(f"Error closing session: {e}")
            raise

    async def get_session(self):
        """Return an active session for database operations."""
        if not self.session:
            logger.error(
                "Session not initialized. Call `init()` before using the session.")
            raise ValueError(
                "Session not initialized. Call `init()` before using the session.")
        return self.session


db = AsyncDatabaseSessions()


async def commit_rollback():
    try:
        await db.commit()
    except Exception:
        await db.rollback()
        raise

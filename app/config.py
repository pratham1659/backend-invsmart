
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

# Database URL and async engine
DATABASE_URL = "postgresql+asyncpg://postgres:mysql@localhost:5432/test"


class AsyncDatabaseSessions:
    def __init__(self) -> None:
        self.session = None
        self.engine = None

    def __getattr__(self, name):
        return getattr(self.session, name)

    def init(self):
        self.engine = create_async_engine(DATABASE_URL, echo=True)
        self.session = sessionmaker(
            self.engine, expire_on_commit=False, class_=AsyncSession)()

    async def create_all(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)


db = AsyncDatabaseSessions()


async def commit_rollback():
    try:
        await db.commit()
    except Exception:
        await db.rollback()
        raise

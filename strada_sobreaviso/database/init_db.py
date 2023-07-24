from database.config import engine
from database.models import Base


async def create_database():
    async with engine.begin() as connection:
        connection.run_sync(Base.metadata.drop_all)

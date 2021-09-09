import sqlalchemy
from sqlalchemy.ext.asyncio import create_async_engine
import asyncio

DatabaseCreated = asyncio.Event()
Database = None

def setup_database(path: str):
    engine = create_async_engine(path, future=True, echo=True)


async def get_database():
    # First waiting for database to be created if hasn't been setup yet
    await DatabaseCreated.wait()
    return Database
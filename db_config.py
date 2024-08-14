import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .main import app
from contextlib import asynccontextmanager
import asyncpg
from fastapi import Depends

# Database initialization
DATABASE = os.path.join(os.path.dirname(__file__), 'timeapi.db')

# Create a SQLite engine
engine = create_engine(f'sqlite:///{DATABASE}', connect_args={"check_same_thread": False})

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

async def get_database():
    pool = await asyncpg.create_pool(DATABASE)
    yield pool
    pool.close()
    await pool.wait_closed()

async def get_db_connection(database: asyncpg.pool.Pool = Depends(get_database)):
    async with database.acquire() as connection:
        yield connection
        
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging
from dotenv import load_dotenv

load_dotenv()

# SQLAlchemy database URL for SQLite

DATABASE_URL = os.getenv("DATABASE_URL")


# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

# Create a configured "Session" class
sessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)

# Create a base class for declarative models
Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()



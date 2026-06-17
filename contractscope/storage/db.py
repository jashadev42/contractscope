from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .schema import Base

DB_PATH = "data/contractscope.db"

engine = create_engine(f"sqlite:///{DB_PATH}")
SessionLocal = sessionmaker(bind=engine)

def init_db() -> None:
    Base.metadata.create_all(engine)
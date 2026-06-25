import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from contractscope.storage.schema import Base

@pytest.fixture
def db_session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    session = Session(engine)

    yield session

    session.close()
    engine.dispose()
import os
from typing import Annotated

import sqlalchemy as _sql
import sqlalchemy.orm as _orm
from fastapi import Depends

DATABASE_URL = os.getenv(
    'DATABASE_URL',
    'postgresql://postgres:postgrespw@localhost:55000/sobreaviso',
)
TEST_DATABASE_URL = os.getenv('TEST_DATABASE_URL', 'false') in ('true', 'yes')

engine = _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base = _orm.declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_deps = Annotated[_orm.Session, Depends(get_db)]

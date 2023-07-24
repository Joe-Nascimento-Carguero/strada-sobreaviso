import sqlalchemy as _sql
import sqlalchemy.orm as _orm

DATABASE_URL = 'postgresql://postgres:postgrespw@localhost:55000/sobreaviso'

engine = _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base = _orm.declarative_base()

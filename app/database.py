
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import String,Integer,Column
from sqlalchemy.orm import DeclarativeBase

# alembic setting
# 1. alembic.ini ==> change sqlalchemy.path value with your database address
# 2. env.py ==> from database import Base
# 3. env.py ==> change the target_meta value with Base.metadata

sql_address = "sqlite:///D:/work projects/alembic_works/app/database.db"
engine = create_engine(sql_address)

local_session = sessionmaker(autoflush=False,autocommit=False,bind=engine)

class Base(DeclarativeBase):
    pass

class person(Base):
    __tablename__ = "person"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String)
    password = Column(String)

def get_data():
    db = local_session()
    try:
        yield db
    finally:
        db.close()

# work with alembic
# add new table ==> alembic revision --autogenerate -m "create table_name table"
# add new column ==> alembic revision --autogenerate -m "added column_name field"

# remove column ==> alembic downgrade (past version)
# the versions are in the versions document - find versions there
# return the column we removed ==> alembic upgrade (the version we want) 

# commit changes ==> alembic upgrade heads
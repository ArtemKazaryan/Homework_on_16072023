from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_NAME = 'sales.db'
LOG_FILE_NAME = 'sales_log.txt'
engine = create_engine(f'sqlite:///{DATABASE_NAME}')

Session = sessionmaker(bind=engine)

Base = declarative_base()


def create_db():
    Base.metadata.create_all(engine)
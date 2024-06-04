from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_NAME = 'Student0iq_sqliteDB.sqlite'

engine = create_engine(f'sqlite:///{DATABASE_NAME}')
Session = sessionmaker(bind=engine)

Base = declarative_base()


#функция создания бд

def create_db():
    Base.metadata.create_all(bind=engine)

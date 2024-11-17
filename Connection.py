from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

user = ''
password = ''
host = ''
database = ''

DATABASE_URI = f"postgresql://{user}:{password}@{host}/{database}"

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

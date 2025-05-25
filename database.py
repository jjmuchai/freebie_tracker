import sqlalchemy
from sqlalchemy import create_engine # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore

# Creates a database engine
engine = create_engine('sqlite:///freebie_tracker.db')

# Creates a declarative base class
Base = declarative_base()

# Creates a session
Session = sessionmaker(bind=engine)
session = Session()

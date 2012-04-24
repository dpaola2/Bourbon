import os

from sqlalchemy import Column, String, Integer, create_engine, Date, ForeignKey, DateTime, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

engine = create_engine(os.environ.get('DATABASE_URL'), echo = False)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'
    id = Column('id', Integer, primary_key = True)
    text = Column('text', Text)

import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class UserPersonalInfo (Base):
    __tablename__ = 'personalInfo'
    name = Column(String(80), nullable = False)
    user_id = Column(String(20), primary_key = True)
    dob = Column(Date, nullable = False)
    gender = Column(String(6))
    email = Column(String(20))
    mobno = Column(String(10))

class UserLoginInfo (Base):
    __tablename__ = 'loginInfo'
    user_id = Column(String(20), primary_key = True)
    password = Column(String(18), nullable = False)


engine = create_engine( 'sqlite:///userinformation.db')

Base.metadata.create_all(engine)
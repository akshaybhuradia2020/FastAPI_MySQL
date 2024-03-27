

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, Integer, String
Base =declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    passwd = Column(String)
    isactive = Column(Boolean, default=True)
    gender = Column(String)
    fullname = Column(String)

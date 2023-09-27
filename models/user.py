#!/usr/bin/python3
"""This is the user class"""
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """This is the class for User
    Attributes:
        email: input email
        password: input password
        first_name: input first name
        last_name: input last name
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

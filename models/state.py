#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """This is the class for State
    Attributes
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("City", cascade='all, delete-orphan', backref="state")

    def __init__(self, *args, **kwargs):
        """Initialize a new State"""
        super().__init__(*args, **kwargs)

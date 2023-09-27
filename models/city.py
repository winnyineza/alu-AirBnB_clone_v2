#!/usr/bin/python3
"""This is the city class"""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    
    # Define the many-to-one relationship with State
    state = relationship("State", back_populates="cities")
    
    # Define the one-to-many relationship with Place
    places = relationship("Place", cascade='all, delete-orphan', backref="city")

    def __init__(self, *args, **kwargs):
        """Initialize a new City"""
        super().__init__(*args, **kwargs)

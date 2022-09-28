#!/usr/bin/python3.8
""" City Module for HBNB project """
from models.base_model import BaseModel, Base, storageType
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
    """
    The city class, contains state ID and name
    """
    if storageType == "db":
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
    else:
        state_id = ""
        name = ""
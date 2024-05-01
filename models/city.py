#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
import models
import os
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class City(BaseModel):
    """ The city class, contains state ID and name """
    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'),
                nullable=False)
        places = relationship('Place', backref='cities',
                cascade='all, delete-orphan')
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)

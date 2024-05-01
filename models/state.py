#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
import models
import os
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class State(BaseModel, Base):
    """ The city class, contains state ID and name """
    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='states',
                cascade='all, delete')
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """returns city instances"""
            city_name = models.storage.all("City").values()
            city_all = []
            for city in city_name:
                if city.state_id == self.id:
                    city_all.append(city)
            return city_all

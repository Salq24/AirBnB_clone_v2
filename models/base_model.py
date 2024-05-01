#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from uuid import uuid4
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import os

tm_format = "%Y-%m-%dT%H:%M:%S.%f"

if os.getenv("HBNB_TYPE_STORAGE") == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""

    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        for k, v in kwargs.items():
            if k == '__class__':
                continue
            setattr(self, k, v)
            if type(self.created_at) is str:
                self.created_at = datetime.strptime(self.created_at, tm_format)
            if type(self.updated_at) is str:
                self.updated_at = datetime.strptime(self.updated_at, tm_format)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self, save_to_disk=False):
        """Convert instance into dict format"""
        n_dict = self.__dict__.copy()
        if 'created_at' in n_dict:
            n_dict['created_at'] = n_dict['created_at'].isoformat()
        if 'updated_at' in n_dict:
            n_dict['updated_at'] = n_dict['updated_at'].isoformat()
        if '_password' in n_dict:
            n_dict['password'] = n_dict['_password'].isoformat()
            n_dict.pop('_password', None)
        if 'reviews' in n_dict:
            n_dict.pop('reviews', None)
        if 'amenities' in n_dict:
            n_dict.pop('amenities', None)
        n_dict['__class__'] = self.__class__.__name__
        n_dict.pop('_sa_instance_state', None)
        if not save_to_disk:
            n_dict.pop('password', None)
        return n_dict

    def delete(self):
        """deletes the current instance from the storage"""
        models.storage.delete(self)

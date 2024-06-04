#!/usr/bin/python3
"""This module defines contains a class dbstorage"""


import models
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.user import User
from models.state import State

classes = {"BaseModel": BaseModel, "Amenity": Amenity,
           "City": City, "Review": Review, "Place": Place,
           "User": User, "State": State}


class DBStorage:
    """This class manages storage of hbnb models in mysql"""
    __engine = None
    __session = None

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        dict_new = {}
        for c in classes:
            if cls is None or cls is c or cls is classes[c]:
                objts = self.__session.query(classes[c]).all()
                for obj in objts:
                    k = obj.__class__.__name__ + "." + obj.id
                    dict_new[k] = obj
            return dict_new

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def save(self):
        """Saves storage dictionary to file"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from objects if inside"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Loads storage dictionary from file"""
        Base.metadata.create_all(self.__engine)
        session_fa = sessionmaker(bind=self.__engine,
                                  expire_on_commit=False)
        self.__session = scoped_session(session_fa)

    def close(self):
        """call reload() method for deserializing
        the JSON file to objects"""
        self.__session.remove()

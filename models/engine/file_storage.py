#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.user import User
from models.state import State

classes = {"BaseModel": BaseModel, "Amenity": Amenity,
           "City": City, "Review": Review, "Place": Place,
           "User": User, "State": State}


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            dict_new = {}
            for k, v in self.__objects.items():
                if cls == v.__class__ or cls == v.__class__.__name__:
                    dict_new[k] = v
            return dict_new
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj is not None:
            k = obj.__class__.__name__ + "." + obj.id
            self.__objects[k] = obj

    def save(self):
        """Saves storage dictionary to file"""
        json_obj = {}
        for k in self.__objects:
            json_obj[k] = self._-objects[k].to_dict()
        with open(self.__file_path, 'w') as r:
            json.dump(json_obj, r)

    def delete(self, obj=None):
        """delete obj from objects if inside"""
        if obj is not None:
            del self.__objects[obj.__class__.__name__ + '.' + obj.id]
            self.save()

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """call reload() method for deserializing
        the JSON file to objects"""
        self.reload()

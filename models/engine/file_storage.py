#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """returns the list of objects of one type of class."""

        if cls is None:
            return self.__obects
        else:
            if isinstance(cls, str):
                cls = eval(cls)
            filtered_obects = {key: obj for key, obj in self.__objects.items() if isinstance(obj, cls)}
            return filtered_objects
    def new(self, obj):
        """Adds new object to storage dictionary"""

        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):

        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""

        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
    def delete(self, obj=None):
        """delete obj from __objects if it’s inside."""

        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]

    def get(self, cls, id):
        """retreive an object."""

        if cls and id:
            if cls in classes.values():
                allobjects = self.all(cls)

                for value in allobjects.values():
                    if value.id == id:
                        return value
            return
        return

    def count(self, cls=None):
        """count the number of objects in storage matchig the classes."""
        
        if not ls:
            instance_ofallclasses = self.all()
            return len(instance_ofallclasses)
        if cls in classe.values():
            allprevclassinstance = selfal(cls)
            return len(allprevclassinstance)
        if cls not in classes.values():
            return

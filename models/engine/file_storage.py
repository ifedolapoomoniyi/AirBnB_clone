#!/usr/bin/python3
"""Defines the File Storage class"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
"""The json module for serialization and deserialization"""


class FileStorage:
    """The FileStorage class that serializes instances to
    a JSON file and deserializes JSON file to instances

    Attributes:
        __file_path(str): path to JSON file
        __objects(dict): empty dictionary but will store all objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """set in __objects with key <obj_class_name>.id"""

        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""

        path = FileStorage.__file_path

        new_obj = {k: FileStorage.__objects[k].to_dict(
            )for k in FileStorage.__objects.keys()}

        with open(path, "w") as file:
            json.dump(new_obj, file)

    def reload(self):
        """deserializes the JSON file to __objects"""

        path = FileStorage.__file_path

        try:
            with open(path) as file:
                object_json = json.load(file)
                for obj in object_json.values():
                    class_name = obj['__class__']
                    del obj['__class__']
                    self.new(eval(class_name)(**obj))

        except FileNotFoundError:
            return

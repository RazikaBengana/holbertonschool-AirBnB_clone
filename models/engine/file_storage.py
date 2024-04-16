#!/usr/bin/python3
"""
This module defines a class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances
"""

import json


class FileStorage:
    """A class that manages storage of all models in the application"""

    __file_path = "file.json"  # Path to the JSON file where objects are stored
    __objects = {}  # Dictionary to store all objects by <class name>.<id>

    def all(self):
        """Return the dictionary '__objects'"""
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the storage dictionary"""
        obj_id = obj.id  # Object id
        obj_name = obj.__class__.__name__  # Object class name
        FileStorage.__objects[obj_name + "." + str(obj_id)] = obj  # Add the object to the storage dictionary

    def save(self):
        """Serialize '__objects' to the JSON file (__file_path)"""
        new_dict = {}

        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()  # Convert object to a dictionary

        with open(FileStorage.__file_path, "w", encoding="UTF8") as file_name:
            json.dump(new_dict, file_name)  # Serialize the dictionary to a JSON file

    def reload(self):
        """Deserializes the JSON file to '__objects' if it exists; otherwise, it does nothing"""
        # Importing necessary models for object creation

        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        try:
            with open(FileStorage.__file_path, encoding="utf-8-sig") as file_name2:
                data = json.load(file_name2)  # Load the JSON file content

                for key, value in data.items():
                    cls = value['__class__']  # Extract the class name of the object
                    # Recreate the instance and add it to the '__objects' dictionary
                    FileStorage.__objects[key] = eval(cls + '(**value)')

        except FileNotFoundError:
            pass  # If the file does not exist, do nothing

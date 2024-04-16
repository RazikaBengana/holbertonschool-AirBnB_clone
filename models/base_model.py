#!/usr/bin/python3
"""
This module defines the BaseModel class, which is the foundation for all other classes in this project;
It includes common attributes and methods that will be inherited
"""

from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """Base class for other models in the application"""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of BaseModel;
        If `kwargs` is not empty, it sets attributes based on `kwargs`;
        Otherwise, it assigns a new UUID, the current datetime to `created_at` and `updated_at`,
        and registers the instance in `storage`
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():

                if key == 'created_at' or key == 'updated_at':
                    cv_str = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, cv_str)

                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    def __str__(self):
        """Return a string representation of the instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Update the `updated_at` attribute with the current datetime and signal the `storage` to save changes
        """
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of the instance's `__dict__`,
        including the class name under key `"__class__"`;
        Converts `created_at` and `updated_at` to string format in ISO standard
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()

        return new_dict

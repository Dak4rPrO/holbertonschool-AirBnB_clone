#!/usr/bin/python3
from datetime import datetime
import uuid
import models
"""from models import storage"""


class BaseModel():
    """ class BaseModel that defines all common
    attributes/methods for other classes """

    def __init__(self, *arg, **kwargs):
        """def init"""
        time_set = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs is not None and len(kwargs) != 0:
            for name, value in kwargs.items():
                if name == 'id':
                    self.id = value
                elif name == 'created_at':
                    self.created_at = datetime.strptime(value, time_set)
                elif name == 'updated_at':
                    self.updated_at = datetime.strptime(value, time_set)
                elif name == "__class__":
                    pass
                else:
                    setattr(self, name, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ def str """
        return(f" [{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """ def save """
        models.storage.save()
        self.updated_at = datetime.now()
        self.created_at = datetime.now()

    def to_dict(self):
        """return a dictionary containning all keys/values of dict"""
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__
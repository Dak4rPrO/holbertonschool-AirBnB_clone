#!/usr/bin/python3
"""class BaseModel"""


from datetime import datetime
import uuid
import sys


class BaseModel:
    
    """ class BaseModel that defines all common attributes/methods for other classes """
    
    def __init__(self, *arg, **kwars):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        """ def str """
        return(f"[BaseModel] ({self.id}) {self.__dict__}")
        
    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return a dictionary containning all keys/values of dict"""
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__
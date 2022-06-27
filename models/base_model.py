#!/usr/bin/python3
"""class BaseModel"""


import uuid
import datetime
import sys


class BaseModel:
    
    """ class BaseModel that defines all common attributes/methods for other classes """
    
    def __init__(self, *arg, **kwars):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    
    def __str__(self):
        """ def str """
        return(f"[BaseModel] ({self.id}) {self.__dict__}")
        
    def save(self):
        self.updated_at = datetime.datetime.now()
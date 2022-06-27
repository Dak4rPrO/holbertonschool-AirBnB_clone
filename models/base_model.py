#!/usr/bin/python3
"""class BaseModel"""


import uuid
import datetime
import sys


class BaseModel:
    
    """ class BaseModel that defines all common attributes/methods for other classes """
    
    def __init__(self, *arg, **kwars):
        self.id = str(uuid.uuid4())
        self.created_ad = datetime.datetime.now()
        self.updated_ad = datetime.datetime.now()
    
    def __str__(self):
        """ def str """
        print(f"[BaseModel] ({self.id}) {self.__dict__}")
        
    def save(self):
        
        
    print(strftime("%Y-%m-%dT%H:%M:%S.%f"))
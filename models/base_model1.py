#!/usr/bin/python3
"""class BaseModel"""


from datetime import datetime
import uuid
import sys


class BaseModel():
    """ class BaseModel that defines all common attributes/methods for other classes """
    
    def __init__(self, *arg, **kwargs):
        """def init"""
        
        if kwargs is not None and len(kwargs) != 0:
            for name, value in kwargs.items():
                if name == ['__class__']:
                    pass
                else:
                   setattr(self, name, value)
                if 'id' in kwargs.keys():
                    self.id = kwargs['id']
                
                if 'created_at' in kwargs.keys():
                    self.created_at = datetime.strptime(kwargs['created_at'],
                                                        time_format)
            if 'updated_at' in kwargs.keys():
                self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                    time_format)
            else:
                return self.__dict__
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            """models.storage.new(self)"""

    def __str__(self):
        """ def str """
        return(f" [{self.__class__.__name__}] ({self.id}) {self.__dict__}")
        
    def save(self):
        """ def save """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return a dictionary containning all keys/values of dict"""
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__
#!/usr/bin/python3

"""from models import storage"""

from datetime import datetime
import uuid
from models import storage


class BaseModel():
    """ class BaseModel that defines all common
    attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        """ Initialization BaseModel """
        time_set = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, time_set)
                elif key == "__class__":
                    pass
                else:
                    setattr(self, name, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ def str """
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """ def save """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all the keys:values ​​of dict """
        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self.created_at.isoformat()        
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy['__class__'] = self.__class__.__name__
        return dict_copy
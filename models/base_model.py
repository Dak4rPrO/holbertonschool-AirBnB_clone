#!/usr/bin/python3
"""class BaseModel"""


import uuid


class BaseModel:
    
    """ class BaseModel that defines all common attributes/methods for other classes """
    
    def __init__(self, id, created_at, updated_at):
        self.id = str(uuid.uuid4())
        
        
    print(date_now.strftime("%A %d %B %Y at %H:%M:%S")
          
    def __str__(self):
        """ def str """
        print(f"[BaseModel] ({self.id}) {self.__dict__}")
#!/usr/bin/python3
""" class city """

from models.base_model import BaseModel


class City(BaseModel):
    """ City initialization """

    state_id = str("")
    name = str("")
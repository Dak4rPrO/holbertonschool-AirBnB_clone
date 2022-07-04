#!/usr/bin/python3
""" class state """

from models.base_model import BaseModel


class State(BaseModel):
    """ State initialization """

    state_id = str("")
    name = str("")
#!/usr/bin/python3
""" public class user """

from models.base_model import BaseModel


class User(BaseModel):
    """ user initialization """

    email = str("")
    password = str("")
    first_name = str("")
    last_name = str("")

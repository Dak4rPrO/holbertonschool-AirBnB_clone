#!/usr/bin/python3
""" public class user """

from models.base_model import BaseModel


class User(BaseModel):
    email = str("")
    password = str("")
    first_name = str("")
    last_name = str("")

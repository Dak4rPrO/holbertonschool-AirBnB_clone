#!/usr/bin/python3
""" init storage """
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
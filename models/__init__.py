#!/usr/bin/python3
"""
Create FileStorage instance for application
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
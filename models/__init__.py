#!/usr/bin/python3
"""Initializing the file storage package from the engine module"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()

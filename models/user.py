#!/usr/bin/python3
"""Module that creates a User class"""

from .base_model import BaseModel


class User(BaseModel):
    """Class for managing user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

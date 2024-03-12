#!/usr/bin/python3
"""Module creates a User class"""

from .base_model import BaseModel


class State(BaseModel):
    """Class for managing state objects"""

    name = ""

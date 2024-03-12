#!/usr/bin/python3
"""Module creates a Review class"""

from .base_model import BaseModel


class Review(BaseModel):
    """Handling class for managing review objects"""

    place_id = ""
    user_id = ""
    text = ""

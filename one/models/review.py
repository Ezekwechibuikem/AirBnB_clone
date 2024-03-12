#!/usr/bin/python3
'''Mmodule that creates a Review class'''
from .base_model import BaseModel


class Review(BaseModel):
    '''Class for managing review objects'''
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        '''Initializes attributes for the review class'''
        super().__init__(*args, **kwargs)

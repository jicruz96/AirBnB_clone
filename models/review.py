#!/usr/bin/python3
"""
Defines Review class
"""

from base_model import BaseModel


class Review(BaseModel):
    """ Review class!

    Attributes:
        place_id (str): ID of place with review (init'd as empty string)
        user_id (str): ID of user leaving review (init'd as empty string)
        text (str): text of review (init'd as empty string)
    """

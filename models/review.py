#!/usr/bin/env python3
"""Defines the class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Defines a class Review with attributes for place, userid, and text"""

    place_id = ""
    user_id = ""
    text = ""

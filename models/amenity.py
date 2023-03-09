#!/usr/bin/env python3
"""Defines a class Amenity that inherits from BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines Amenity with name as an attribute"""

    name = ""

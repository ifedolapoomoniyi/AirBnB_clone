#!/usr/bin/env python3
"""Defines a class City that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Defines City with state_id and name as attributes"""

    state_id = ""
    name = ""

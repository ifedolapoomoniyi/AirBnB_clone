#!/usr/bin/env python3
""" Defines a class User that inherits from basemodel"""

from models.base_model import BaseModel


class User(BaseModel):
    """Defines a class User"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

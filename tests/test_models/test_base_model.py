#!/usr/bin/python3
"""Defines unittests for model/base_model.py

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""

import os
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class"""

    def test_instantiation(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1, b2)

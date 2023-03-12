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
from time import sleep


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class"""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_type(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_type(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_type(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_object_instance_created_time(self):
        self.assertNotEqual(datetime.now(), BaseModel().created_at)

    def test_object_instance_updated_time(self):
        self.assertNotEqual(datetime.now(), BaseModel().updated_at)

    def test_object_isinstance(self):
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)

    def test_object_instance_not_equal(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1, b2)

    def test_object_unique_id(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_models_different_created_at(self):
        b1 = BaseModel()
        sleep(0.05)
        b2 = BaseModel()
        self.assertLess(b1.created_at, b2.created_at)

    def test_models_different_updated_at(self):
        b1 = BaseModel()
        sleep(0.05)
        b2 = BaseModel()
        self.assertLess(b1.updated_at, b2.updated_at)

if __name__ == '__main__':
    unittest.main()

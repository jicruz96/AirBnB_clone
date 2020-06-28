#!/usr/bin/python3
""" Contains unittests for BaseModel class """
import unittest
import os
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModelClass(unittest.TestCase):
    """ Tests BaseModel class """
    # create object instance of BaseModel class
    obj = BaseModel()

    def test_init(self):
        """ Tests init method """
        # check if object is an instance of BaseModel
        self.assertIsInstance(obj, BaseModel)
        # check if dictionary contains all expected attributes
        # __dict__ only contains set attributes so this checks if set
        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)
        # check if public instance attributes are of correct type
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str(self):
        """ Tests __str__ method """

    def test_save(self):
        """ Tests save method """

    def test_to_dict(self):
        """ Tests to_dict method """

#!/usr/bin/python3
""" Contains unittests for FileStorage class """
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorageClass(unittest.TestCase):
    """ Tests FileStorage class """

    def test_all(self):
        """ Tests all method """
        # create storage instance and instance of BaseModel
        storage = FileStorage()
        obj = BaseModel()
        __objects = storage.all()
        # test that storage.all() returns dictionary
        self.assertIsInstance(__objects, dict)
        # test that BaseModel instance in dictionary of objects
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertIn(key, __objects)
        # test that the value in dictionary is of same type and equal to obj
        self.assertEqual(obj, __objects[key])
        self.assertIsInstance(__objects[key], BaseModel)

    def test_new(self):
        """ Tests new method """
        # create storage instance and instance of BaseModel
        storage = FileStorage()
        obj = BaseModel()
        # create dictionary to set obj values to with **kwargs
        new_dict = {}
        new_dict["id"] = "012345"
        new_dict["created_at"] = "1995-2-2T10:23:35.123450"
        new_dict["updated_at"] = "1999-1-4T7:15:05.543210"
        # create instance with **kwargs and test that object is not in __objects
        obj2 = BaseModel(**new_dict)
        key = "{}.{}".format(type(obj2).__name__, obj2.id)
        self.assertNotIn(key, storage.all())
        # obj2 is reset to new instance of BaseModel and
        # should be added to dictionary with new
        obj2 = BaseModel()
        key = "{}.{}".format(type(obj2).__name__, obj2.id)
        __objects = storage.all()
        self.assertIn(key, __objects)
        self.assertEqual(obj2, __objects[key])

    def test_save(self):
        """ Tests save method """

    def test_reload(self):
        """ Tests reload method """

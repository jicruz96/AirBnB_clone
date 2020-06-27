#!/usr/bin/python3
"""
Defines the FileStorage class
"""

import json


class FileStorage():
    """ serializes to / deserializes from a JSON file

        Attributes:
            __file_path (str): path to JSON file
            __objects (dict): will store objects by class.id
    """
    __file_path = "file.JSON"  # string - path to JSON file
    __objects = {}  # dictionary - empty but will store objects by class.id

    def all(self):
        """ returns __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id
            Args:
                obj (:obj:`BaseModel`): object to add to __objects dictionary
         """
        key = "{}.{}".format(cls.__name__(obj), obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """ serializes __object to the JSON file """
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        """ deserializes JSON file to __objects

        Note:
            if JSON file (__file_path) does not exist, nothing is done.
        """
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.loads(f.read())
        except Exception as err:
            pass

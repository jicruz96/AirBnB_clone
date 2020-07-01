#!/usr/bin/python3
"""
Defines the FileStorage class
"""

from json import loads, dumps
from os.path import exists


class FileStorage():
    """ serializes to / deserializes from a JSON file

        Attributes:
            __file_path (str): path to JSON file
            __objects (dict): will store objects by class.id
    """
    __file_path = "file.json"  # string - path to JSON file
    __objects = {}  # dictionary - empty but will store objects by class.id

    def all(self):
        """ returns dictionary of all saved objects """
        return self.__objects

    def new(self, obj):
        """
        stores obj in __objects dictionary:
                key = "<obj class name>.id"
                value = obj.to_dict()

            Args:
                obj (:obj:`BaseModel`): object to add to __objects
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __object to the JSON file """
        dict_of_dicts = {}
        for key, value in self.__objects.items():
            dict_of_dicts[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            f.write(dumps(dict_of_dicts))

    def reload(self):
        """ deserializes JSON file to __objects

        Note:
            if JSON file (__file_path) does not exist, nothing is done.
        """

        if exists(self.__file_path) is False:
            return

        with open(self.__file_path, 'r') as f:
            dicts = loads(f.read())

        classes = self.known_classes()
        self.__objects = {}
        for instance_id, dict in dicts.items():
            cls_name = instance_id.split('.')[0]
            cls = classes[cls_name]
            self.__objects[instance_id] = cls(**dict)

    @staticmethod
    def known_classes():
        from ..base_model import BaseModel
        from ..amenity import Amenity
        from ..city import City
        from ..place import Place
        from ..review import Review
        from ..state import State
        from ..user import User

        classes = {
            "Amenity": Amenity,
            "BaseModel": BaseModel,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User,
        }

        return classes

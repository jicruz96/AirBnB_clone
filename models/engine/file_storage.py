#!/usr/bin/python3
""" Defines the FileStorage class
    """


class FileStorage():
    """ serializes to / deserializes from a JSON file 

        Attributes:
            __file_path (str): path to JSON file
            __objects (dict): will store objects by class.id
    """
    __file_path  # string - path to JSON file
    __objects  # dictionary - empty but will store objects by class.id

    def all(self):
        """ returns __objects """

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id

            Args:
                obj (:obj:`BaseModel`): object to add to __objects dictionary
         """

    def save(self):
        """ serializes __object to the JSON file """

    def reload(self):
        """ deserializes JSON file to __objects

        Note:
            if JSON file (__file_path) does not exist, nothing is done.
        """

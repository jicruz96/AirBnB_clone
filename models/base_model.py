#!/usr/bin/python3
"""
    defines BaseModel class
"""

from models import storage
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
        defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        our public instance attributes are:
            id (str): will be assigned with uuid.uuid4() converted to string
            created_at: will be assigned datetime
            updated_at: assigned with datetime each object is changed
        *args won't be used
        if kwargs is not empty:
            each key corresponds to an attribute name
            (except don't add __class__)
            values of dictionary correspond to values of attributes
            note: convert created_at and updated_at into datetime object
        else:
            storage.new() to add new instance to storage
        """
        if kwargs:
            for kw in kwargs:
                if kw == "id":
                    self.id = kwargs[kw]
                if kw == "created_at":
                    self.created_at = datetime.strptime(kwargs[kw],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                if kw == "updated_at":
                    self.updated_at = datetime.strptime(kwargs[kw],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        printing string rep with class name, self.id, self.__dict__
        """
        str_rep = "[{}] ({}) {}".format(self.__class__, self.id, self.__dict__)
        return (str_rep)

    def save(self):
        """
        update the updated_at attribute with the current datetime
        call save(self) method of storage: storage.save()
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary with all keys/values of __dict__ of instance

        1. use self.__dict__ to make dictionary
        2. manually add __class__ to dictionary
        Note:
            - convert created_at and updated_at to ISO format
                - use isoformat()
        """
        dict_rep = {}
        for key in self.__dict__:
            if key == "converted_at" or key == "updated_at":
                dict_rep[key] = datetime.isoformat(self.__dict__[key])
            else:
                dict_rep[key] = self.__dict__[key]
        dict_rep[__class__] = self.__class__

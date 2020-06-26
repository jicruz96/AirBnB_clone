#!/usr/bin/python3
"""
    defines BaseModel class
"""

from __init__ import storage


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
            each key corresponds to an attribute name (except don't add __class__)
            values of dictionary correspond to values of attributes
            note: convert created_at and updated_at into datetime object
        else:
            storage.new() to add new instance to storage
        """

    def __str__(self):
        """
        printing string rep with class name, self.id, self.__dict__
        """

    def save(self):
        """
        update the updated_at attribute with the current datetime
        call save(self) method of storage: storage.save()
        """

    def to_dict(self):
        """
        returns a dictionary with all keys/values of __dict__ of instance 

        1. use self.__dict__ to make dictionary
        2. manually add __class__ to dictionary
        Note:
            - convert created_at and updated_at to ISO format
                - use isorformat()
        """

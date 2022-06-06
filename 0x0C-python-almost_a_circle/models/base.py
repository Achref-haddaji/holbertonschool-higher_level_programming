#!/usr/bin/python3
""" Base module """
import json


class Base:
    """ Base class """
    __nb_objects = 0  # private class attrib

    def __init__(self, id=None):
        """
        Init method
        Args:
            id(int): given id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """

        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

#!/usr/bin/python3
""" class Base """

import json


class Base:
    """ Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes attributes for class Base
        Args:
            id: public instance attribute
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries
        Args:
            list_dictionaries: a list of dictionaries
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return (json.dumps(list_dictionaries))

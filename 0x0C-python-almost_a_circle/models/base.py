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

    @classmethod
    def save_to_file(cls, list_objs):
        """write file.json"""
        fun = cls.__name__
        filname = fun + ".json"
        new_list = []
        with open(filname, mode="w", encoding="utf-8") as f:
            if list_objs is None:
                f.write(cls.to_json_string([]))
            else:
                for i in list_objs:
                    new_list.append(i.to_dictionary)
                f.write(cls.to_json_string(list_objs))

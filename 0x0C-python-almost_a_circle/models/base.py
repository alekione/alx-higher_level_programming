#!/usr/bin/python3
""" Base class initialization """
import json


class Base:
    """ Attributes for the base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize field id for all classes and objects """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves object instances into a file """
        if list_objs is None or len(list_objs) == 0:
            file_name = "Base.json"
        else:
            file_name = list_objs[0].__class__.__name__ + ".json"
        obj_lst = []
        for item in list_objs:
            obj_lst.append(item.to_dictionary())
        js = Base.to_json_string(obj_lst)
        with open(file_name, "w", encoding="UTF8") as fp:
            fp.write(js)

    @staticmethod
    def from_json_string(json_string):
        """ decodes a json string passed into it """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ creates new objects from a given dictionary """
        if cls.__name__ == "Square":
            obj = cls(5)
        if cls.__name__ == "Rectangle":
            obj = cls(4, 5)
        obj.update(dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """ loads instances from  a file """
        filename = cls.__name__ + ".json"
        lst = []
        try:
            fp = open(filename, mode="r", encoding="UTF8")
            fp.close()
        except Exception:
            return []
        else:
            fp = open(filename, mode="r", encoding="UTF8")
            js = Base.from_json_string(fp.read())
            for item in js:
                obj = cls.create(item)
                lst.append(obj)
            fp.close()
        return lst

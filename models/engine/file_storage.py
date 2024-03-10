#!/usr/bin/python3
"""File storage class"""
import json


class FileStorage:
    """FileStorage class"""

    __file_path = "file.json"  # path to the JSON file
    __objects = {}  # empty but will store all objects by <class name>.id

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        dict_obj = {}
        for key, value in FileStorage.__objects.items():
            dict_obj[key] = value.to_dict()
            with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
                json.dump(dict_obj, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.base_model import BaseModel

        defined_classes = {"BaseModel": BaseModel}
        try:
            with open(FileStorage.__file_path, "r") as file:
                deserialize = json.load(file)

                for obj_values in deserialize.values():
                    class_name = obj_values["__class__"]
                    class_obj = defined_classes[class_name]
                    self.new(class_obj(**obj_values))
        except FileNotFoundError:
            pass

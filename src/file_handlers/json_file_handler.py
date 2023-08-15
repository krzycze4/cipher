"""
A module to represent a JSON file handler.

Classes:
    JsonFileHandler(FileHandler)
"""
import json
from typing import List, Union, Dict

from src.factories.text_factory import TextFactory
from src.file_handlers.file_handler import FileHandler
from src.texts.text import Text


class JsonFileHandler(FileHandler):
    """
    A class to represent a JSON file handler.

    Methods
    _______
    __init__()
        constructs all the necessary attributes for the file handler object
    save_to_file(buffer: List[Text]) -> None
        saves buffer to json
    load_from_file() -> None
        loads json data from file to list
    prepare_data_to_load_to_buffer() -> Union[None, List[Text]]
        prepare json data to load to buffer
    create_list_of_texts()
        creates list of texts object from json data
    """
    def __init__(self):
        """
        A method constructs all the necessary attributes for the file handler object.

        Attributes
        __________
        self.path: Union[None, str]
            path of the json file
        self.json_data: Union[None, List[Dict[str, str]]] = None
            json data
        self.texts: List[Text] = []
            list of objects Text
        """
        self.path: Union[None, str] = None
        self.json_data: Union[None, List[Dict[str, str]]] = None
        self.texts: List[Text] = []

    def save_to_file(self, buffer: List[Text]) -> None:
        """
        A method saves buffer to json.

        Parameters
        __________
        buffer: List[Text]
            list of Text objects

        Returns
        _______
        None
        """
        self.load_from_file()

        with open(self.path, "w") as file:
            for text in buffer:
                text_data = {
                    "content": text.content,
                    "rot_type": text.rot_type,
                    "status": text.status
                }
                self.json_data.append(text_data)
            json.dump(self.json_data, file, indent=4)
            buffer.clear()

    def load_from_file(self) -> None:
        """
        A method loads json data from file to list.

        Returns
        _______
        None
        """
        file_name = input("File name: ")
        self.path = file_path = fr"C:\Users\komputer Synka\Documents\IT\devMentoring\cipher\src\files\{file_name}.json"


        try:
            with open(file_path, "r") as jsonfile:
                self.json_data = json.load(jsonfile)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            self.json_data = []

    def prepare_data_to_load_to_buffer(self) -> Union[None, List[Text]]:
        """
        A method loads json data to buffer.

        Returns
        _______
        None
        """
        self.load_from_file()
        self.create_list_of_texts()
        return self.texts

    def create_list_of_texts(self):
        """
        A method creates list of Text objects.

        Returns
        _______
        None
        """
        for text in self.json_data:
            content = text.get("content")
            rot_type = text.get("rot_type")
            status = text.get("status")

            text_obj = TextFactory().create_object(content=content,
                                                   rot_type=rot_type,
                                                   status=status)
            self.texts.append(text_obj)

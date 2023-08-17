# flake8: noqa: E501
"""A module to represent class JsonFileHandler"""
import json
from typing import List, Union, Dict

from src.file_handlers.file_handler import FileHandler
from src.texts.text import Text


class JsonFileHandler(FileHandler):
    def __init__(self):
        self.path: Union[None, str] = None
        self.json_data: Union[None, List[Dict[str, str]]] = None
        self.texts: List[object] = []

    def save_to_file(self, buffer: List[Text]) -> None:
        """
        A method saves buffer to json.

        Parameters
        __________
        buffer: List[Text]
            list of Text objects
        """
        self.load_from_file()

        with open(self.path, "w") as file:
            for text in buffer:
                text_data = {
                    "content": text.content,
                    "rot_type": text.rot_type,
                    "status": text.status,
                }
                self.json_data.append(text_data)
            json.dump(self.json_data, file, indent=4)

    def load_from_file(self) -> None:
        """A method loads json data from file to list."""
        file_name = input("File name: ")
        self.path = (
            file_path
        ) = rf"C:\Users\komputer Synka\Documents\IT\devMentoring\cipher\src\files\{file_name}.json"

        try:
            with open(file_path, "r") as jsonfile:
                self.json_data = json.load(jsonfile)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            self.json_data = []

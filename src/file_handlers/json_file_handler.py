import json
from typing import List, Union, Dict

from src.factories.text_factory import TextFactory
from src.file_handlers.file_handler import FileHandler
from src.texts.text import Text


class JsonFileHandler(FileHandler):

    def __init__(self):
        self.path: Union[None, str] = None
        self.json_data: Union[None, List[Dict[str, str]]] = None
        self.texts: List[Text] = []

    def save_to_file(self, buffer: List[Text]) -> None:
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
        file_name = input("File name: ")
        self.path = file_path = fr"C:\Users\komputer Synka\Documents\IT\devMentoring\cipher\src\files\{file_name}.json"

        try:
            with open(file_path, "r") as jsonfile:
                self.json_data = json.load(jsonfile)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            self.json_data = []

    def load_to_buffer(self) -> Union[None, List[Text]]:
        self.load_from_file()
        self.transform_data_to_object()
        return self.texts

    def transform_data_to_object(self):
        for text in self.json_data:
            content = text.get("content")
            rot_type = text.get("rot_type")
            status = text.get("status")

            text_obj = TextFactory().create_object(content=content,
                                                   rot_type=rot_type,
                                                   status=status)
            self.texts.append(text_obj)

from src.factories.abstract_factory import AbstractFactory
from src.text.text import Text


class TextFactory(AbstractFactory):
    def create_object(self, content: str, rot_type: str, status: str) -> Text:
        return Text(_content=content, _rot_type=rot_type, _status=status)

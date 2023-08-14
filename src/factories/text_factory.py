from src.factories.abstract_factory import AbstractFactory
from src.texts.text import Text


class TextFactory(AbstractFactory):
    """
    Class is Abstract Factory.
    Inheritance from AbstractFactory class.
    """
    @classmethod
    def create_object(cls, content: str, rot_type: str, status: str) -> Text:
        """
        It's class method.
        Create and return Text object.
        :param content: str
        :param rot_type: str
        :param status: str
        :return: Text
        """
        return Text(_content=content, _rot_type=rot_type, _status=status)

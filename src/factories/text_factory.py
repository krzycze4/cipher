"""
A module to represent a TextFactory class.

Classes:
    TextFactory(AbstractFactory)
"""
from src.factories.abstract_factory import AbstractFactory
from src.texts.text import Text


class TextFactory(AbstractFactory):
    """
    A class to represent a texts factory.

    Methods
    _______
    create_object(*args: str)
        a class method returns Text object
    """
    @classmethod
    def create_object(cls, content: str, rot_type: str, status: str) -> Text:
        """
        A class method returns Text object.

        Parameters
        __________
        content: str
            text to encrypt or decrypt
        rot_type: str
            type of used cipher
        status: str
            status of cryption

        Returns
        _______
        Text
            object of Text
        """
        return Text(_content=content, _rot_type=rot_type, _status=status)

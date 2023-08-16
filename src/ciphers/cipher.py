"""A module to represent an abstract class Cipher"""
from abc import ABC, abstractmethod


class Cipher(ABC):
    """
    A class to represent a cipher

    Methods
    _______
    __str__() -> None:
        returns class name
    encrypt(text_content: str) -> str
        raises NotImplementedError
    decrypt(text_content: str) -> str:
        raises NotImplementedError
    """

    def __str__(self) -> str:
        """
        A method returns class name

        Returns
        _______
        str
            class name
        """
        return f"{self.__class__.__name__}"

    @abstractmethod
    def encrypt(self, text_content: str):
        """
        An abstract method encrypts text

        Parameters
        __________
        text_content: str
            text to encrypt
        """
        raise NotImplementedError

    @abstractmethod
    def decrypt(self, text_content: str):
        """
        An abstract method decrypts text

        Parameters
        __________
        text_content: str
            text to decrypt
        """
        raise NotImplementedError

from abc import ABC, abstractmethod


class Cipher(ABC):
    """
    This is Abstract Class Cipher
    """
    def __str__(self):
        return f"{self.__class__.__name__}"

    @abstractmethod
    def encrypt(self, text_content: str) -> str:
        """
        This is abstract method. Encrypt parameter text_content.
        :param text_content: str
        :raise: NotImplementedError
        """
        raise NotImplementedError

    @abstractmethod
    def decrypt(self, text_content: str) -> str:
        """
        This is abstract method. Decrypt parameter text_content.
        :param text_content: str
        :return: NotImplementedError
        """
        raise NotImplementedError

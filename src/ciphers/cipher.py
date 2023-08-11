from abc import ABC, abstractmethod


class Cipher(ABC):
    def __str__(self):
        return f"{self.__class__.__name__}"

    @abstractmethod
    def encrypt(self, text_content: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def decrypt(self, text_content: str) -> str:
        raise NotImplementedError

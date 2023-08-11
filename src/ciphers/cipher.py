from abc import ABC, abstractmethod


class Cipher(ABC):
    @abstractmethod
    def encrypt(self, text_content: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def decrypt(self, text_content: str) -> str:
        raise NotImplementedError

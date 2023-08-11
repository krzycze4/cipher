from abc import ABC, abstractmethod


class Cipher(ABC):
    @abstractmethod
    def encrypt(self):
        raise NotImplementedError

    @abstractmethod
    def decrypt(self):
        raise NotImplementedError

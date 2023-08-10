from abc import ABC, abstractmethod


class Manager(ABC):
    @abstractmethod
    def run(self):
        raise NotImplementedError

    @abstractmethod
    def encrypt_text(self):
        raise NotImplementedError

    @abstractmethod
    def decrypt_text(self):
        raise NotImplementedError

    @abstractmethod
    def save_buffer(self):
        raise NotImplementedError

    @abstractmethod
    def load_to_buffer(self):
        raise NotImplementedError

    @abstractmethod
    def exit(self):
        raise NotImplementedError

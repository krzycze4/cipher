from abc import ABC, abstractmethod


class FileHandler(ABC):
    @abstractmethod
    def save_to_file(self):
        raise NotImplementedError

    @abstractmethod
    def load_from_file(self):
        raise NotImplementedError

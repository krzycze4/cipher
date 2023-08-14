from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    Abstract Factory Class
    """
    @abstractmethod
    def create_object(self, *args):
        raise NotImplementedError

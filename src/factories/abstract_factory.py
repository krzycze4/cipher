from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    Abstract Factory Class
    """
    @abstractmethod
    def create_object(self, *args):
        """
        It's abstract method
        """
        raise NotImplementedError

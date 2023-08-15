"""
A module to represent an AbstractFactory class.

Classes:
    AbstractFactory(ABC)
"""
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    A class to represent an abstract factory.

    Methods
    _______
    create_object(*args: str)
        an abstract method raises NotImplementedError
    """
    @abstractmethod
    def create_object(self, *args):
        """
        An abstract method raises NotImplementedError.

        Parameters
        __________
        *args: str
            arguments to create an object

        Raises
        ______
        NotImplementedError
        """
        raise NotImplementedError

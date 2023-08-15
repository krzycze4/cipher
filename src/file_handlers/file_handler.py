"""
A module to represent an abstract class of file handler.

Classes:
    FileHandler(ABC)
"""
from abc import ABC, abstractmethod


class FileHandler(ABC):
    """
    An abstract class to represent a file handler.

    Methods
    _______
    save_to_file(*args)
        an abstract method raises NotImplementedError
    load_from_file(*args)
        an abstract method raises NotImplementedError
    """
    @abstractmethod
    def save_to_file(self, *args):
        """
        An abstract method raises NotImplementedError.

        Parameters
        __________
        *args
            arguments to save to file

        Raises
        ______
        NotImplementedError
        """
        raise NotImplementedError

    @abstractmethod
    def load_from_file(self):
        """
        An abstract method raises NotImplementedError.

        Raises
        ______
        NotImplementedError
        """
        raise NotImplementedError

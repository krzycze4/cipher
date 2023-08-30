"""A module to represent an abstract class of file handler"""
from abc import ABC, abstractmethod
from typing import List

from texts import Text


class FileHandler(ABC):
    @abstractmethod
    def save_to_file(self, buffer: List[Text]):
        """
        An abstract method raises NotImplementedError.

        Parameters
        __________
        buffer: List[Text]
            list of Text objects to save to file
        """
        raise NotImplementedError

    @abstractmethod
    def load_from_file(self):
        """An abstract method raises NotImplementedError."""
        raise NotImplementedError

"""A module to represent an abstract class Manager."""
from abc import ABC, abstractmethod


class Manager(ABC):
    @abstractmethod
    def run(self):
        """An abstract method runs program"""
        raise NotImplementedError

    @abstractmethod
    def exit(self):
        """An abstract method exits program"""
        raise NotImplementedError

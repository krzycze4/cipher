"""
A module to represent an abstract class Manager.

Classes:
    Manager(ABC)
"""
from abc import ABC, abstractmethod


class Manager(ABC):
    """
    An abstract class to represent a manager.

    Methods
    _______
    run()
        raises NotImplementedError
    exit()
        raises NotImplementedError
    """
    @abstractmethod
    def run(self):
        """
        An abstract method raises NotImplementedError

        Raises
        ______
        NotImplementedError
        """
        raise NotImplementedError

    @abstractmethod
    def exit(self):
        """
        An abstract method raises NotImplementedError

        Raises
        ______
        NotImplementedError
        """
        raise NotImplementedError

"""A module to represent an abstract class Menu"""
from abc import ABC, abstractmethod


class Menu(ABC):
    """An abstract class to represent menu."""

    @staticmethod
    @abstractmethod
    def display_main_menu() -> None:
        """A static abstract method raises NotImplementedError."""
        raise NotImplementedError

"""
A module to represent an abstract class Menu.

Classes:
    Menu
"""
from abc import ABC, abstractmethod


class Menu(ABC):
    """
    A class to represent program menu.

    Methods
    _______
    display_welcome() -> None
        displays welcome text
    display_main_menu() -> None
        display main menu
    display_cipher_menu() -> None
        display cipher menu
    """

    @staticmethod
    @abstractmethod
    def display_welcome() -> None:
        """
        A static abstract method raises NotImplementedError.

        Raises
        ______
        NotImplementedError
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def display_main_menu() -> None:
        """
        A static abstract method raises NotImplementedError.

        Raises
        ______
        NotImplementedError
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def display_cipher_menu() -> None:
        """
        A static abstract method raises NotImplementedError.

        Raises
        ______
        NotImplementedError
        """
        raise NotImplementedError

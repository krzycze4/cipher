"""A module to represent a class CipherMenu"""
from src.menus.menu import Menu


class CipherMenu(Menu):
    """A class to represent program menu"""

    @staticmethod
    def display_welcome() -> None:
        """A static method displays welcome text"""
        print("\nWelcome to Cipher")

    @staticmethod
    def display_main_menu() -> None:
        """A static method displays main menu"""
        print("\nMenu:")
        print("1. Encrypt texts")
        print("2. Decrypt texts")
        print("3. Save buffer")
        print("4. Load to buffer")
        print("5. Exit")

    @staticmethod
    def display_cipher_menu() -> None:
        """A static method displays cipher menu"""
        print("\nChoose cipher:")
        print("1. ROT13")
        print("2. ROT47")

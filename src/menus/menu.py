"""
A module to represent a class Menu.

Classes:
    Menu
"""


class Menu:
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
    def display_welcome() -> None:
        """
        A static method displays welcome text.

        Returns
        _______
        None
        """
        print("\nWelcome to Cipher")

    @staticmethod
    def display_main_menu() -> None:
        """
        A static method displays main menu.

        Returns
        _______
        None
        """
        print("\nMenu:")
        print("1. Encrypt texts")
        print("2. Decrypt texts")
        print("3. Save buffer")
        print("4. Load to buffer")
        print("5. Exit")

    @staticmethod
    def display_cipher_menu() -> None:
        """
        A static method displays cipher menu.

        Returns
        _______
        None
        """
        print("\nChoose cipher:")
        print("1. ROT13")
        print("2. ROT47")

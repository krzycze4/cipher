from typing import Union

from src.exceptions.exceptions import OutOfRangeError


class Menu:
    def __init__(self) -> None:
        self.choice: Union[None, int] = None

    def take_choice(self, limit: int) -> None:
        while True:
            try:
                choice = int(input("\nChoice: "))
                if choice not in range(1, limit + 1):
                    raise OutOfRangeError
            except (ValueError, OutOfRangeError):
                print(f"Only numbers from 1 to {limit}")
                self.choice = None
            else:
                self.choice = choice
                break

    @staticmethod
    def display_welcome() -> None:
        print("\nWelcome to Cipher")

    @staticmethod
    def display_main_menu() -> None:
        print("\nMenu:")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Save buffer")
        print("4. Load to buffer")
        print("5. Exit")

    @staticmethod
    def display_cipher_menu() -> None:
        print("\nChoose cipher:")
        print("1. ROT13")
        print("2. ROT47")

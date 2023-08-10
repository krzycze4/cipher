from src.exceptions.exceptions import OutOfRangeError


class Menu:
    def __init__(self) -> None:
        self.choice = None

    def take_choice(self) -> None:
        while True:
            try:
                choice = int(input("\nChoice: "))
                if choice not in range(1, 6):
                    raise OutOfRangeError
            except (ValueError, OutOfRangeError):
                print("Only numbers from 1 to 5")
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

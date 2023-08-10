class Menu:

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

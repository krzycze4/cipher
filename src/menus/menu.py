class Menu:

    @staticmethod
    def display_welcome() -> None:
        print("\nWelcome to Cipher")

    @staticmethod
    def display_main_menu() -> None:
        print("\nMenu:")
        print("1. Encrypt texts")
        print("2. Decrypt texts")
        print("3. Save buffer")
        print("4. Load to buffer")
        print("5. Exit")

    @staticmethod
    def display_cipher_menu() -> None:
        print("\nChoose cipher:")
        print("1. ROT13")
        print("2. ROT47")

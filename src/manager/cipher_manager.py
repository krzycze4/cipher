from typing import Union

from src.ciphers.cipher_rot13 import CipherROT13
from src.ciphers.cipher_rot47 import CipherROT47
from src.exceptions.exceptions import OutOfRangeError
from src.factories.text_factory import TextFactory
from src.manager.manager import Manager
from src.menu.menu import Menu


class CipherManager(Manager):
    def __init__(self):
        self.menu = Menu()
        self.choice: Union[None, int] = None
        self.cipher_rot13 = CipherROT13()
        self.cipher_rot47 = CipherROT47()
        self.menu_options = {
            1: self.encrypt_text,
            2: self.decrypt_text,
            3: self.save_buffer,
            4: self.load_to_buffer,
            5: self.exit
        }
        self.cipher_options = {
            1: self.cipher_rot13,
            2: self.cipher_rot47
        }
        self.buffer = []

    def run(self):
        self.menu.display_welcome()
        while True:
            self.menu.display_main_menu()
            self.take_choice(limit=len(self.menu_options))
            self.execute()

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

    def execute(self):
        self.menu_options.get(self.choice)()

    def encrypt_text(self):
        user_input = input("\nText content: ")
        self.menu.display_cipher_menu()
        self.take_choice(limit=len(self.cipher_options))
        content = self.cipher_options.get(self.choice).encrypt(text_content=user_input)
        status = "encrypted"
        rot_type = str(self.cipher_options.get(self.choice))
        text = TextFactory().create_object(content=content, rot_type=rot_type, status=status)
        print(text.content)
        self.buffer.append(text)

    def decrypt_text(self):
        user_input = input("\nText content: ")
        self.menu.display_cipher_menu()
        self.take_choice(limit=len(self.cipher_options))
        content = self.cipher_options.get(self.choice).decrypt(text_content=user_input)
        status = "decrypted"
        rot_type = str(self.cipher_options.get(self.choice))
        text = TextFactory().create_object(content=content, rot_type=rot_type, status=status)
        print(text.content)
        self.buffer.append(text)

    def save_buffer(self):
        # zapytaj o nazwę pliku do zapisu
        # context manager z jsonem, flaga "a"
        # zapis
        pass

    def load_to_buffer(self):
        # zapytaj o nazwę pliku do zapisu
        # context manager z jsonem, flaga "a"
        # odczyt do buffera
        pass

    def exit(self):
        exit()

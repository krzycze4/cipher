from typing import Union

from src.ciphers.cipher_rot13 import CipherROT13
from src.ciphers.cipher_rot47 import CipherROT47
from src.exceptions.exceptions import OutOfRangeError, EmptyInputError
from src.factories.text_factory import TextFactory
from src.file_handlers.json_file_handler import JsonFileHandler
from src.managers.manager import Manager
from src.menus.menu import Menu


class CipherManager(Manager):
    def __init__(self):
        self.menu = Menu()
        # podziel self.choice na dwa (menu oraz cipher)
        self.choice: Union[None, int] = None
        self.content_input: Union[None, str] = None
        self.file_handler = JsonFileHandler()
        self.buffer = []
        self.menu_options = {
            1: self.crypt_text,
            2: self.crypt_text,
            3: self.save_buffer,
            4: self.load_to_buffer,
            5: self.exit
        }
        self.cipher_options = {
            1: CipherROT13(),
            2: CipherROT47()
        }
        self.status = {
            1: "encrypted",
            2: "decrypted"
        }
        self.crypt_options = {
            1: self.encrypt_text,
            2: self.decrypt_text
        }

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

    def crypt_text(self) -> None:
        self.take_input_content()
        self.menu.display_cipher_menu()
        self.take_choice(limit=len(self.cipher_options))

        rot_type = str(self.cipher_options.get(self.choice))
        status = self.status.get(self.choice)
        content = self.crypt_options.get(self.choice)()
        text = TextFactory().create_object(content=content, rot_type=rot_type, status=status)

        print(text.content)
        self.buffer.append(text)

    def take_input_content(self):
        while True:
            try:
                user_input = input("\nText content: ")
                if len(user_input.strip()) == 0:
                    raise EmptyInputError
            except EmptyInputError:
                print("Empty input")
            else:
                self.content_input = user_input
                break

    def encrypt_text(self) -> str:
        return self.cipher_options.get(self.choice).encrypt(text_content=self.content_input)

    def decrypt_text(self) -> str:
        return self.cipher_options.get(self.choice).decrypt(text_content=self.content_input)

    def save_buffer(self):
        self.file_handler.save_to_file(self.buffer)

    def load_to_buffer(self):
        self.buffer += self.file_handler.load_to_buffer()

    def exit(self):
        exit()

# flake8: noqa: E501
"""A module to represent a class CipherManager"""
from copy import copy
from typing import Union, Dict, Callable

from buffers import Buffer
from ciphers import Cipher
from ciphers import CipherROT13
from ciphers import CipherROT47
from exceptions import OutOfRangeError, EmptyInputError
from file_handlers import JsonFileHandler
from manager import Manager
from menus import CipherMenu
from texts import Text


class CipherManager(Manager):
    """
    A class to represent a cipher manager object.

    Methods
    _______
    run(self) -> None
        runs program
    take_choice(self, limit: int) -> None
        takes user choice
    execute(self)
        executes chosen option in menu
    crypt_text(self) -> None
        creates Text object and add it to self.buffer
    take_input_content(self) -> None
        takes user's input
    encrypt_text(self) -> str
        returns encrypted text
    decrypt_text(self) -> str
        returns decrypted text
    save_buffer(self) -> None
        saves self.buffer to json file and clear it
    load_to_buffer(self) -> None
        loads json file to self.buffer
    exit(self) -> None
        exits the program
    """

    def __init__(self):
        self.choice: Union[None, int] = None
        self.content_input: Union[None, str] = None
        self.file_handler = JsonFileHandler()
        self.buffer = Buffer()
        self.menu_options: Dict[int, Callable] = {
            1: self.crypt_text,
            2: self.crypt_text,
            3: self.save_buffer,
            4: self.load_to_buffer,
            5: self.exit,
        }
        self.cipher_options: Dict[int, Cipher] = {1: CipherROT13(), 2: CipherROT47()}
        self.status: Dict[int, str] = {1: "encrypted", 2: "decrypted"}
        self.crypt_options: Dict[int, Callable] = {
            1: self.encrypt_text,
            2: self.decrypt_text,
        }

    def run(self) -> None:
        """A method runs program."""
        CipherMenu().display_welcome()
        while True:
            CipherMenu().display_main_menu()
            self.take_choice(limit=len(self.menu_options))
            self.execute()

    def take_choice(self, limit: int) -> None:
        """
        A method takes user choice.

        Parameters
        __________
        limit: int
            set right edge of the range
        """
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

    def execute(self) -> None:
        """A method executes chosen option in menu."""
        self.menu_options.get(self.choice)()

    def crypt_text(self) -> None:
        """A method creates Text object and add it to self.buffer."""
        cipher_choice = copy(self.choice)
        self.take_input_content()
        CipherMenu().display_cipher_menu()
        self.take_choice(limit=len(self.cipher_options))

        status: str = self.status.get(cipher_choice)
        rot_type: str = str(self.cipher_options.get(self.choice))
        content: str = self.crypt_options.get(self.choice)()
        text = Text(content=content, rot_type=rot_type, status=status)
        self.buffer.add(text)

    def take_input_content(self) -> None:
        """A method takes user's input."""
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
        """
        A method returns encrypted text.

        Returns
        _______
        str
            encrypted text
        """
        return self.cipher_options.get(self.choice).encrypt(
            text_content=self.content_input
        )

    def decrypt_text(self) -> str:
        """
        A method returns decrypted text.

        Returns
        _______
        str
            decrypted text
        """
        return self.cipher_options.get(self.choice).decrypt(
            text_content=self.content_input
        )

    def save_buffer(self) -> None:
        """A method saves self.buffer to json file and clear it."""
        self.file_handler.save_to_file(self.buffer.list)
        self.buffer.clear()

    def load_to_buffer(self) -> None:
        """A method loads json file to self.buffer."""
        self.file_handler.load_from_file()
        for json_text in self.file_handler.json_data:
            self.buffer.add(Text.create_from_dict(json_text))

    def exit(self) -> None:
        """A method exits the program."""
        exit()

from src.ciphers.cipher_rot13 import CipherROT13
from src.ciphers.cipher_rot47 import CipherROT47
from src.factories.text_factory import TextFactory
from src.manager.manager import Manager
from src.menu.menu import Menu


class CipherManager(Manager):
    def __init__(self):
        self.menu = Menu()
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
            self.menu.take_choice(limit=len(self.menu_options))
            self.execute()

    def execute(self):
        self.menu_options.get(self.menu.choice)()

    def encrypt_text(self):
        user_input = input("\nText content: ")
        self.menu.display_cipher_menu()
        self.menu.take_choice(limit=len(self.cipher_options))
        content = self.cipher_options.get(self.menu.choice).encrypt(user_input)
        status = "encrypted"
        rot_type = str(self.cipher_options.get(self.menu.choice))
        text = TextFactory().create_object(content, rot_type, status)
        self.buffer.append(text)

    def decrypt_text(self):
        # tutaj będziesz pobierał content
        # pobierał rot
        # użyj szyfru - TODO DECRYPTION
        # określał status
        # użyjesz tutaj factory
        # dodasz do buffer
        pass

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

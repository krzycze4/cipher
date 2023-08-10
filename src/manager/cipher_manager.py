from src.manager.manager import Manager
from src.menu.menu import Menu


class CipherManager(Manager):
    def __init__(self):
        self.menu = Menu()
        self.options = {
            1: self.encrypt_text,
            2: self.decrypt_text,
            3: self.save_buffer,
            4: self.load_to_buffer,
            5: self.exit
        }

    def run(self):
        self.menu.display_welcome()
        while True:
            self.menu.display_main_menu()
            self.menu.take_choice()
            self.execute()

    def execute(self):
        self.options.get(self.menu.choice)()

    def encrypt_text(self):
        pass

    def decrypt_text(self):
        pass

    def save_buffer(self):
        pass

    def load_to_buffer(self):
        pass

    def exit(self):
        exit()


"""A module to execute the whole project."""
from src.managers.cipher_manager import CipherManager


def main():
    manager = CipherManager()
    manager.run()


if __name__ == "__main__":
    main()

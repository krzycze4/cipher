"""
A module to execute the whole project.

Functions:
    main()
"""
from src.managers.cipher_manager import CipherManager


def main():
    """A method starts cipher project"""
    manager = CipherManager()
    manager.run()


if __name__ == '__main__':
    main()
    
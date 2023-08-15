"""
A module to represent a class of cipher ROT47.
"Shift" means shift in ASCII encoding system.

Classes:
    CipherROT47(Cipher)
"""
from src.ciphers.cipher import Cipher


class CipherROT47(Cipher):
    """
    A class to represent a cipher ROT47.

    Variables
    _______________
    cipher_range

    Methods
    _______
    encrypt(text_content: str) -> str
        a class method returns encrypted text
    decrypt(text_content: str) -> str
        a class method returns decrypted text
    create_new_string(text_content: str, char_shift: int) -> str
        a class method returns crypted or decrypted text
    shift_char(char: str, char_shift: int) -> str
        a static method returns shifted character
    """
    cipher_range = range(ord("!"), ord("~") + 1)

    @classmethod
    def encrypt(cls, text_content: str) -> str:
        """
        A class method returns encrypted text.

        Parameters
        __________
        text_content: str
            text to encrypt

        Returns
        _______
        str
            encrypted text
        """
        return cls.create_new_string(text_content=text_content, char_shift=47)

    @classmethod
    def decrypt(cls, text_content: str) -> str:
        """
        A class method returns decrypted text.

        Parameters
        __________
        text_content: str
            text to decrypt

        Returns
        _______
        str
            decrypted text
        """
        return cls.create_new_string(text_content=text_content, char_shift=-47)

    @classmethod
    def create_new_string(cls, text_content: str, char_shift: int) -> str:
        """
        A class method returns crypted or decrypted text.

        Parameters
        __________
        text_content: str
            text to decrypt
        char_shift: int
            number of shifts character

        Returns
        _______
        str
            encrypted or decrypted text
        """
        encrypted_chars = []
        for char in text_content:
            encrypted_chars.append(cls.shift_char(char=char, char_shift=char_shift))
        return "".join(encrypted_chars)

    @classmethod
    def shift_char(cls, char: str, char_shift: int) -> str:
        """
        A static method shifts character in text_content
        with declared char_shift if it's in range between
        "!" and "~" included.

        Parameters
        __________
        text_content: str
            text to decrypt
        char_shift: int
            number of shifts character

        Returns
        _______
        str
            shifted or (if char not in range) not shifted character
        """
        char_decimal = ord(char)
        if char_decimal in cls.cipher_range:
            char_decimal = char_decimal + char_shift
            if char_decimal > ord("~"):
                char_decimal = ord("!") + char_decimal - ord("~") - 1
            elif char_decimal < ord("!"):
                char_decimal = ord("~") - (ord("!") - char_decimal) + 1
        return chr(char_decimal)

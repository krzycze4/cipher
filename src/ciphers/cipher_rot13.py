"""
A module to represent a class of cipher ROT13.
"Shift" means shift in ASCII encoding system.

Classes:
    CipherROT13(Cipher)
"""
from src.ciphers.cipher import Cipher


class CipherROT13(Cipher):
    """
    A class to represent a cipher ROT13.

    Variables
    _______________
    upper_range
    lower_range

    Methods
    _______
    encrypt(text_content: str) -> str
        a class method returns encrypted text
    decrypt(text_content: str) -> str
        a class method returns decrypted text
    create_new_string(text_content: str, char_shift: int) -> str
        a class method returns crypted or decrypted text
    shift_char(char: str, char_shift: int, letter_a: str, letter_z: str) -> str
        a static method returns shifted character
    """
    upper_range = range(ord("A"), ord("Z") + 1)
    lower_range = range(ord("a"), ord("z") + 1)

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
        return cls.create_new_string(text_content=text_content, char_shift=13)

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
        return cls.create_new_string(text_content=text_content, char_shift=-13)

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
        crypted_chars = []
        for char in text_content:
            if ord(char) in cls.upper_range:
                crypted_chars.append(cls.shift_char(char=char,
                                                      char_shift=char_shift,
                                                      letter_a="A",
                                                      letter_z="Z"))
            elif ord(char) in cls.lower_range:
                crypted_chars.append(cls.shift_char(char=char,
                                                      char_shift=char_shift,
                                                      letter_a="a",
                                                      letter_z="z"))
        return "".join(crypted_chars)

    @staticmethod
    def shift_char(char: str, char_shift: int, letter_a: str, letter_z: str) -> str:
        """
        A static method shifts character in text_content with declared char_shift if
        it's in range between letter_a and letter_b included.

        Parameters
        __________
        text_content: str
            text to decrypt
        char_shift: int
            number of shifts character
        letter_a: str
            character a or A
        letter_z: str
            character z or Z

        Returns
        _______
        str
            shifted or (if char not in range) not shifted character
        """
        char_decimal = ord(char)
        if char_decimal in range(ord(letter_a), ord(letter_z) + 1):
            char_decimal = char_decimal + char_shift
            if char_decimal > ord(letter_z):
                char_decimal = ord(letter_a) + char_decimal - ord(letter_z) - 1
            elif char_decimal < ord(letter_a):
                char_decimal = ord(letter_z) - (ord(letter_a) - char_decimal) + 1
        return chr(char_decimal)

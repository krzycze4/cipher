from src.ciphers.cipher import Cipher


UPPER_RANGE = range(ord("A"), ord("Z") + 1)
LOWER_RANGE = range(ord("a"), ord("z") + 1)


class CipherROT13(Cipher):

    @classmethod
    def encrypt(cls, text_content: str) -> str:
        return cls.create_new_string(text_content=text_content, char_shift=13)

    @classmethod
    def decrypt(cls, text_content: str) -> str:
        return cls.create_new_string(text_content=text_content, char_shift=-13)

    @classmethod
    def create_new_string(cls, text_content: str, char_shift: int) -> str:
        encrypted_chars = []
        for char in text_content:
            if ord(char) in UPPER_RANGE:
                encrypted_chars.append(cls.shift_char(char=char,
                                                      char_shift=char_shift,
                                                      letter_a="A",
                                                      letter_z="Z"))
            elif ord(char) in LOWER_RANGE:
                encrypted_chars.append(cls.shift_char(char=char,
                                                      char_shift=char_shift,
                                                      letter_a="a",
                                                      letter_z="z"))
        return "".join(encrypted_chars)

    @staticmethod
    def shift_char(char: str, char_shift: int, letter_a: str, letter_z: str) -> str:
        char_decimal = ord(char)
        if char_decimal in range(ord(letter_a), ord(letter_z) + 1):
            char_decimal = char_decimal + char_shift
            if char_decimal > ord(letter_z):
                char_decimal = ord(letter_a) + char_decimal - ord(letter_z) - 1
            elif char_decimal < ord(letter_a):
                char_decimal = ord(letter_z) - (ord(letter_a) - char_decimal) + 1
        return chr(char_decimal)

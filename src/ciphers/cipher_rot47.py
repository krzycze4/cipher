from src.ciphers.cipher import Cipher


CIPHER_RANGE = range(ord("!"), ord("~") + 1)


class CipherROT47(Cipher):
    @classmethod
    def encrypt(cls, text_content: str) -> str:
        return cls.create_new_string(text_content=text_content, char_shift=47)

    @classmethod
    def decrypt(cls, text_content: str) -> str:
        return cls.create_new_string(text_content=text_content, char_shift=-47)

    @classmethod
    def create_new_string(cls, text_content: str, char_shift: int) -> str:
        encrypted_chars = []
        for char in text_content:
            encrypted_chars.append(cls.shift_char(char=char, char_shift=char_shift))
        return "".join(encrypted_chars)

    @staticmethod
    def shift_char(char: str, char_shift: int) -> str:
        char_decimal = ord(char)
        if char_decimal in CIPHER_RANGE:
            char_decimal = char_decimal + char_shift
            if char_decimal > ord("~"):
                char_decimal = ord("!") + char_decimal - ord("~") - 1
            elif char_decimal < ord("!"):
                char_decimal = ord("~") - (ord("!") - char_decimal) + 1
        return chr(char_decimal)

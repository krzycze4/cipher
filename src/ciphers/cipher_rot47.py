from src.ciphers.cipher import Cipher


class CipherROT47(Cipher):
    @classmethod
    def encrypt(cls, text_content: str) -> str:
        encrypted_chars = []
        for char in text_content:
            encrypted_chars.append(cls.shift_char(char=char, char_shift=47))
        return "".join(encrypted_chars)

    @classmethod
    def decrypt(cls, text_content: str) -> str:
        encrypted_chars = []
        for char in text_content:
            encrypted_chars.append(cls.shift_char(char=char, char_shift=-47))
        output = "".join(encrypted_chars)
        return output

    @staticmethod
    def shift_char(char: str, char_shift: int) -> str:
        char_decimal = ord(char)
        if char_decimal in range(ord("!"), ord("~") + 1):
            char_decimal = char_decimal + char_shift
            if char_decimal > ord("~"):
                char_decimal = ord("!") + char_decimal - ord("~") - 1
            elif char_decimal < ord("!"):
                char_decimal = ord("~") - (ord("!") - char_decimal) + 1
        return chr(char_decimal)

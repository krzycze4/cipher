from src.ciphers.cipher import Cipher


CIPHER_RANGE = range(ord("!"), ord("~") + 1)


class CipherROT47(Cipher):
    """
    This is class CipherROT47.
    Inheritance from abstract class Cipher.
    Rotate characters in word by 47 in decimal ascii notation
    in forward(encrypt) or backward(decrypt).
    Example: "A" -> "p",
             "!" -> "P",
             "z -> "K",
    """
    @classmethod
    def encrypt(cls, text_content: str) -> str:
        """
        This is class method.
        Encrypt parameter text_content and return encrypted string.
        :param text_content: str.
        :return: str
        """
        return cls.create_new_string(text_content=text_content, char_shift=47)

    @classmethod
    def decrypt(cls, text_content: str) -> str:
        """
        This is class method.
        Decrypt parameter text_content and return decrypted string.
        :param text_content: str.
        :return: str
        """
        return cls.create_new_string(text_content=text_content, char_shift=-47)

    @classmethod
    def create_new_string(cls, text_content: str, char_shift: int) -> str:
        """
        This is class method.
        Method takes parameter text_content and shift particular letter in
        text_content by char_shift. Then create and return new string.
        :param text_content: str
        :param char_shift: int
        :return: str
        """
        encrypted_chars = []
        for char in text_content:
            encrypted_chars.append(cls.shift_char(char=char, char_shift=char_shift))
        return "".join(encrypted_chars)

    @staticmethod
    def shift_char(char: str, char_shift: int) -> str:
        """
        This is static method.
        Method takes parameter char and determines if it should be shifted.
        Shift takes place if char is in range(ord("!"), ord("~") + 1)
        Return shifted char if it's in cipher range or return parameter char
        :param char: str
        :param char_shift: int
        :return: str
        """
        char_decimal = ord(char)
        if char_decimal in CIPHER_RANGE:
            char_decimal = char_decimal + char_shift
            if char_decimal > ord("~"):
                char_decimal = ord("!") + char_decimal - ord("~") - 1
            elif char_decimal < ord("!"):
                char_decimal = ord("~") - (ord("!") - char_decimal) + 1
        return chr(char_decimal)

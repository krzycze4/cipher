from src.ciphers.cipher import Cipher


class CipherROT13(Cipher):
    """
    This is class CipherROT13.
    Inheritance from abstract class Cipher.
    Rotate characters in word by 13
    in forward(encrypt) or backward(decrypt).
    Example: "A" -> "N",
             "a" -> "n",
             "N -> "A",
             "n" -> "a"
    """
    upper_range = range(ord("A"), ord("Z") + 1)
    lower_range = range(ord("a"), ord("z") + 1)

    @classmethod
    def encrypt(cls, text_content: str) -> str:
        """
        This is class method.
        Encrypt parameter text_content and return encrypted string.
        :param text_content: str.
        :return: str
        """
        return cls.create_new_string(text_content=text_content, char_shift=13)

    @classmethod
    def decrypt(cls, text_content: str) -> str:
        """
        This is class method.
        Decrypt parameter text_content and return decrypted string.
        :param text_content: str.
        :return: str
        """
        return cls.create_new_string(text_content=text_content, char_shift=-13)

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
            if ord(char) in cls.upper_range:
                encrypted_chars.append(cls.shift_char(char=char,
                                                      char_shift=char_shift,
                                                      letter_a="A",
                                                      letter_z="Z"))
            elif ord(char) in cls.lower_range:
                encrypted_chars.append(cls.shift_char(char=char,
                                                      char_shift=char_shift,
                                                      letter_a="a",
                                                      letter_z="z"))
        return "".join(encrypted_chars)

    @staticmethod
    def shift_char(char: str, char_shift: int, letter_a: str, letter_z: str) -> str:
        """
        This is static method.
        Method takes parameter char and determines if it should be shifted.
        Shift takes place if char is in range(ord("A"), ord("Z") + 1)
        or in range(ord("a"), ord("z") + 1)
        Return shifted char if it's in cipher range or return parameter char
        :param char: str
        :param char_shift: int
        :param letter_a: str.
        :param letter_z: str.
        :return: str
        """
        char_decimal = ord(char)
        if char_decimal in range(ord(letter_a), ord(letter_z) + 1):
            char_decimal = char_decimal + char_shift
            if char_decimal > ord(letter_z):
                char_decimal = ord(letter_a) + char_decimal - ord(letter_z) - 1
            elif char_decimal < ord(letter_a):
                char_decimal = ord(letter_z) - (ord(letter_a) - char_decimal) + 1
        return chr(char_decimal)

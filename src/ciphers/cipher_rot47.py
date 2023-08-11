from src.ciphers.cipher import Cipher


class CipherROT47(Cipher):
    def encrypt(self, text_content: str) -> str:
        encrypted_chars = []
        for char in text_content:
            char_decimal = ord(char)
            if char_decimal in range(ord("!"), ord("~") + 1):
                char_decimal = char_decimal + 47
                if char_decimal > ord("~"):
                    char_decimal = ord("!") + char_decimal - ord("~") - 1
            encrypted_chars.append(chr(char_decimal))
        output = "".join(encrypted_chars)
        return output

    def decrypt(self, text_content: str) -> str:
        encrypted_chars = []
        for char in text_content:
            char_decimal = ord(char)
            if char_decimal in range(ord("!"), ord("~") + 1):
                char_decimal = char_decimal - 47
                if char_decimal < ord("~"):
                    char_decimal = ord("!") - char_decimal + ord("~") + 1
            encrypted_chars.append(chr(char_decimal))
        output = "".join(encrypted_chars)
        return output

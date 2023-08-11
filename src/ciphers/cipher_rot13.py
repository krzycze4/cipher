from src.ciphers.cipher import Cipher


class CipherROT13(Cipher):
    def encrypt(self, text_content: str) -> str:
        encrypted_chars = []
        for char in text_content:
            char_decimal = ord(char)
            if char_decimal in range(ord("A"), ord("Z") + 1):
                char_decimal = char_decimal + 13
                if char_decimal > ord("Z"):
                    char_decimal = ord("A") + char_decimal - ord("Z") - 1
            elif char_decimal in range(ord("a"), ord("z") + 1):
                char_decimal = char_decimal + 13
                if char_decimal > ord("z"):
                    char_decimal = ord("a") + char_decimal - ord("z") - 1
            encrypted_chars.append(chr(char_decimal))
        output = "".join(encrypted_chars)
        return output

    def decrypt(self, text_content: str) -> str:
        encrypted_chars = []
        for char in text_content:
            char_decimal = ord(char)
            if char_decimal in range(ord("A"), ord("Z") + 1):
                char_decimal = char_decimal - 13
                if char_decimal < ord("A"):
                    char_decimal = ord("Z") - char_decimal + ord("A") + 1
            elif char_decimal in range(ord("a"), ord("z") + 1):
                char_decimal = char_decimal - 13
                if char_decimal < ord("a"):
                    char_decimal = ord("z") - char_decimal + ord("a") + 1
            encrypted_chars.append(chr(char_decimal))
        output = "".join(encrypted_chars)
        return output

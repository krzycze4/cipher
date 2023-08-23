# flake8: noqa: E501
import pytest

from src.ciphers.cipher_rot13 import CipherROT13


class TestCipherROT13:
    def setup_method(self):
        self.cipher = CipherROT13()

    @pytest.mark.shift_char
    @pytest.mark.parametrize("char", ["a", "b", "k", "m"])
    def test_should_return_shifted_plus_13_lowercase_when_shift_char_from_a_to_m(
        self, char, char_shift=13, letter_a="a", letter_z="z"
    ):
        shifted_char = self.cipher.shift_char(char, char_shift, letter_a, letter_z)
        assert shifted_char == chr(ord(char) + char_shift)

    @pytest.mark.shift_char
    @pytest.mark.parametrize("char", ["n", "o", "y", "z"])
    def test_should_return_shifted_plus_13_lowercase_when_shift_char_from_n_to_z(
        self, char, char_shift=13, letter_a="a", letter_z="z"
    ):
        shifted_char = self.cipher.shift_char(char, char_shift, letter_a, letter_z)
        assert shifted_char == chr(char_shift + ord(char) + ord("a") - ord("z") - 1)

    @pytest.mark.shift_char
    @pytest.mark.parametrize("char", ["a", "b", "k", "m"])
    def test_should_return_shifted_minus_13_lowercase_when_shift_char_from_a_to_m(
        self, char, char_shift=-13, letter_a="a", letter_z="z"
    ):
        shifted_char = self.cipher.shift_char(char, char_shift, letter_a, letter_z)
        assert shifted_char == chr(char_shift + ord(char) - ord("a") + ord("z") + 1)

    @pytest.mark.shift_char
    @pytest.mark.parametrize("char", ["n", "o", "y", "z"])
    def test_should_return_shifted_minus_13_lowercase_when_shift_char_from_n_to_z(
        self, char, char_shift=-13, letter_a="a", letter_z="z"
    ):
        shifted_char = self.cipher.shift_char(char, char_shift, letter_a, letter_z)
        assert shifted_char == chr(ord(char) + char_shift)

    @pytest.mark.shift_char
    @pytest.mark.parametrize("char", ["A", "B", "K", "M"])
    def test_should_return_shifted_plus_13_uppercase_when_shift_char_from_A_to_M(
        self, char, char_shift=13, letter_a="A", letter_z="Z"
    ):
        shifted_char = self.cipher.shift_char(char, char_shift, letter_a, letter_z)
        assert shifted_char == chr(ord(char) + char_shift)

    @pytest.mark.shift_char
    @pytest.mark.parametrize("char", ["N", "P", "Y", "Z"])
    def test_should_return_shifted_plus_13_uppercase_when_shift_char_from_N_to_Z(
        self, char, char_shift=13, letter_a="A", letter_z="Z"
    ):
        shifted_char = self.cipher.shift_char(char, char_shift, letter_a, letter_z)
        assert shifted_char == chr(char_shift + ord(char) + ord("a") - ord("z") - 1)

    @pytest.mark.shift_char
    @pytest.mark.parametrize("char", ["A", "B", "K", "M"])
    def test_should_return_shifted_minus_13_uppercase_when_shift_char_from_A_to_M(
        self, char, char_shift=-13, letter_a="A", letter_z="Z"
    ):
        shifted_char = self.cipher.shift_char(char, char_shift, letter_a, letter_z)
        assert shifted_char == chr(char_shift + ord(char) - ord("a") + ord("z") + 1)

    @pytest.mark.shift_char
    @pytest.mark.parametrize("char", ["N", "P", "Y", "Z"])
    def test_should_return_shifted_minus_13_uppercase_when_shift_char_from_N_to_Z(
        self, char, char_shift=-13, letter_a="A", letter_z="Z"
    ):
        shifted_char = self.cipher.shift_char(char, char_shift, letter_a, letter_z)
        assert shifted_char == chr(ord(char) + char_shift)

    @pytest.mark.shift_char
    @pytest.mark.parametrize("char", ["!", "~"])
    def test_should_return_same_special_sign_when_shift_char_special_sign(
        self, char, char_shift=-13, letter_a="A", letter_z="Z"
    ):
        shifted_char = self.cipher.shift_char(char, char_shift, letter_a, letter_z)
        assert shifted_char == char

    @pytest.mark.create_new_string
    def test_should_return_string_when_create_new_string_execute_lowercase(
        self, mocker, text_content="abc", char_shift=13
    ):
        mocker.patch(
            "src.ciphers.cipher_rot13.CipherROT13.shift_char",
            side_effect=["n", "o", "p"],
        )
        new_string = self.cipher.create_new_string(text_content, char_shift)
        assert new_string == "nop"

    @pytest.mark.create_new_string
    def test_should_return_string_when_create_new_string_execute_uppercase(
        self, mocker, text_content="ABC", char_shift=13
    ):
        mocker.patch(
            "src.ciphers.cipher_rot13.CipherROT13.shift_char",
            side_effect=["N", "O", "P"],
        )
        new_string = self.cipher.create_new_string(text_content, char_shift)
        assert new_string == "NOP"

    @pytest.mark.encrypt
    def test_should_return_string_when_encrypt_text(self, mocker, text_content="abc"):
        mocker.patch(
            "src.ciphers.cipher_rot13.CipherROT13.create_new_string", return_value="nop"
        )
        decrypted_string = self.cipher.encrypt(text_content)
        assert decrypted_string == "nop"

    @pytest.mark.decrypt
    def test_should_return_string_when_decrypt_text(self, mocker, text_content="abc"):
        mocker.patch(
            "src.ciphers.cipher_rot13.CipherROT13.create_new_string", return_value="nop"
        )
        decrypted_string = self.cipher.decrypt(text_content)
        assert decrypted_string == "nop"

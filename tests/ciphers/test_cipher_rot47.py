# flake8: noqa: E501
import pytest

from src.ciphers.cipher_rot47 import CipherROT47  #


class TestCipherROT13:
    def setup_method(self):
        self.cipher = CipherROT47()

    @pytest.mark.shift_char
    @pytest.mark.parametrize("char", ["!", "A", "O"])
    def test_should_return_shifted_char_plus_47_when_shift_char_between_exclamation_point_and_upper_o(
        self, char, char_shift=47
    ):
        shifted_char = self.cipher.shift_char(char, char_shift)
        assert shifted_char == chr(ord(char) + char_shift)

    @pytest.mark.shift_char
    @pytest.mark.parametrize("char", ["P", "a", "~"])
    def test_should_return_shifted_char_plus_47_when_shift_char_between_upper_p_and_tilde(
        self, char, char_shift=47
    ):
        shifted_char = self.cipher.shift_char(char, char_shift)
        assert shifted_char == chr(ord(char) + char_shift - (ord("~") - ord("!")) - 1)

    @pytest.mark.shift_char
    @pytest.mark.parametrize("char", ["!", "A", "O"])
    def test_should_return_shifted_char_minus_47_when_shift_char_between_exclamation_point_and_upper_o(
        self, char, char_shift=-47
    ):
        shifted_char = self.cipher.shift_char(char, char_shift)
        assert shifted_char == chr(ord(char) + char_shift + (ord("~") - ord("!")) + 1)

    @pytest.mark.shift_char
    @pytest.mark.parametrize("char", ["P", "a", "~"])
    def test_should_return_shifted_char_plus_47_when_shift_char_between_upper_p_and_tilde(
        self, char, char_shift=-47
    ):
        shifted_char = self.cipher.shift_char(char, char_shift)
        assert shifted_char == chr(ord(char) + char_shift)

    @pytest.mark.create_new_string
    def test_should_return_string_when_create_new_string_execute(
        self, mocker, text_content="abc", char_shift=47
    ):
        mocker.patch(
            "src.ciphers.cipher_rot47.CipherROT47.shift_char",
            side_effect=["2", "3", "4"],
        )
        new_string = self.cipher.create_new_string(text_content, char_shift)
        assert new_string == "234"

    @pytest.mark.encrypt
    def test_should_return_string_when_decrypt_text(self, mocker, text_content="abc"):
        mocker.patch(
            "src.ciphers.cipher_rot47.CipherROT47.create_new_string", return_value="234"
        )
        decrypted_string = self.cipher.encrypt(text_content)
        assert decrypted_string == "234"

    @pytest.mark.decrypt
    def test_should_return_string_when_decrypt_text(self, mocker, text_content="234"):
        mocker.patch(
            "src.ciphers.cipher_rot47.CipherROT47.create_new_string", return_value="abc"
        )
        decrypted_string = self.cipher.decrypt(text_content)
        assert decrypted_string == "abc"

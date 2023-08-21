# flake8: noqa: E501
import pytest

from src.ciphers.cipher_rot47 import CipherROT47


class TestCipherROT13:
    @pytest.fixture
    def cipher(self):
        return CipherROT47

    @pytest.mark.shift_char
    @pytest.mark.parametrize("char, char_shift", [("a", 47)])
    def test_should_return_2_when_shift_char_lower_a(self, char, char_shift, cipher):
        shifted_char = cipher.shift_char(char, char_shift)
        assert shifted_char == "2"  # nosec

    @pytest.mark.shift_char
    @pytest.mark.parametrize("char, char_shift", [("2", -47)])
    def test_should_return_lower_a_when_shift_char_digit_2(
        self, char, char_shift, cipher
    ):
        shifted_char = cipher.shift_char(char, char_shift)
        assert shifted_char == "a"  # nosec

    @pytest.mark.shift_char
    @pytest.mark.parametrize("char, char_shift", [(" ", 47)])
    def test_should_return_whitespace_when_shift_char_whitespace(
        self, char, char_shift, cipher
    ):
        shifted_char = cipher.shift_char(char, char_shift)
        assert shifted_char == " "  # nosec

    @pytest.mark.shift_char
    @pytest.mark.parametrize("char, char_shift", [("~", 47)])
    def test_should_return_upper_o_when_shift_char_tilde(
        self, char, char_shift, cipher
    ):
        shifted_char = cipher.shift_char(char, char_shift)
        assert shifted_char == "O"  # nosec

    @pytest.mark.shift_char
    @pytest.mark.parametrize("char, char_shift", [("O", -47)])
    def test_should_return_tilde_when_shift_char_upper_o(
        self, char, char_shift, cipher
    ):
        shifted_char = cipher.shift_char(char, char_shift)
        assert shifted_char == "~"  # nosec

    @pytest.mark.create_new_string
    @pytest.mark.parametrize("text_content, char_shift", [("abc", 47)])
    def test_should_return_string_when_create_new_string_execute(
        self, text_content, char_shift, cipher, mocker
    ):
        mocker.patch(
            "src.ciphers.cipher_rot47.CipherROT47.shift_char",
            side_effect=["2", "3", "4"],
        )
        new_string = cipher.create_new_string(text_content, char_shift)
        assert new_string == "234"  # nosec

    @pytest.mark.encrypt
    @pytest.mark.parametrize("text_content", ["abc"])
    def test_should_return_string_when_decrypt_text(self, cipher, mocker, text_content):
        mocker.patch(
            "src.ciphers.cipher_rot47.CipherROT47.create_new_string", return_value="234"
        )
        decrypted_string = cipher.encrypt(text_content)
        assert decrypted_string == "234"  # nosec

    @pytest.mark.decrypt
    @pytest.mark.parametrize("text_content", ["234"])
    def test_should_return_string_when_decrypt_text(self, cipher, mocker, text_content):
        mocker.patch(
            "src.ciphers.cipher_rot47.CipherROT47.create_new_string", return_value="abc"
        )
        decrypted_string = cipher.decrypt(text_content)
        assert decrypted_string == "abc"  # nosec

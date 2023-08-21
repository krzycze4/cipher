# flake8: noqa: E501
import pytest

from src.ciphers.cipher_rot13 import CipherROT13


class TestCipherROT13:
    @pytest.fixture
    def cipher(self):
        return CipherROT13

    @pytest.mark.shift_char
    @pytest.mark.parametrize(
        "char, char_shift, letter_a, letter_z", [("a", 13, "a", "z")]
    )
    def test_should_return_lower_n_when_shift_char_lower_a(
        self, char, char_shift, letter_a, letter_z, cipher
    ):
        shifted_char = cipher.shift_char(char, char_shift, letter_a, letter_z)
        assert shifted_char == "n"  # nosec

    @pytest.mark.shift_char
    @pytest.mark.parametrize(
        "char, char_shift, letter_a, letter_z", [("n", -13, "a", "z")]
    )
    def test_should_return_lower_a_when_shift_char_lower_n(
        self, char, char_shift, letter_a, letter_z, cipher
    ):
        shifted_char = cipher.shift_char(char, char_shift, letter_a, letter_z)
        assert shifted_char == "a"  # nosec

    @pytest.mark.shift_char
    @pytest.mark.parametrize(
        "char, char_shift, letter_a, letter_z", [("A", 13, "A", "Z")]
    )
    def test_should_return_upper_n_when_shift_char_upper_a(
        self, char, char_shift, letter_a, letter_z, cipher
    ):
        shifted_char = cipher.shift_char(char, char_shift, letter_a, letter_z)
        assert shifted_char == "N"  # nosec

    @pytest.mark.shift_char
    @pytest.mark.parametrize(
        "char, char_shift, letter_a, letter_z", [("N", -13, "A", "Z")]
    )
    def test_should_return_upper_a_when_shift_char_upper_n(
        self, char, char_shift, letter_a, letter_z, cipher
    ):
        shifted_char = cipher.shift_char(char, char_shift, letter_a, letter_z)
        assert shifted_char == "A"  # nosec

    @pytest.mark.shift_char
    @pytest.mark.parametrize(
        "char, char_shift, letter_a, letter_z", [("9", -13, "A", "Z")]
    )
    def test_should_return_same_digit_when_shift_char_digit(
        self, char, char_shift, letter_a, letter_z, cipher
    ):
        shifted_char = cipher.shift_char(char, char_shift, letter_a, letter_z)
        assert shifted_char == "9"  # nosec

    @pytest.mark.shift_char
    @pytest.mark.parametrize(
        "char, char_shift, letter_a, letter_z", [("!", -13, "A", "Z")]
    )
    def test_should_return_same_special_sign_when_shift_char_special_sign(
        self, char, char_shift, letter_a, letter_z, cipher
    ):
        shifted_char = cipher.shift_char(char, char_shift, letter_a, letter_z)
        assert shifted_char == "!"  # nosec

    @pytest.mark.shift_char
    @pytest.mark.parametrize(
        "char, char_shift, letter_a, letter_z", [("z", 13, "a", "z")]
    )
    def test_should_return_lower_m_when_shift_lower_z(
        self, char, char_shift, letter_a, letter_z, cipher
    ):
        shifted_char = cipher.shift_char(char, char_shift, letter_a, letter_z)
        assert shifted_char == "m"  # nosec

    @pytest.mark.create_new_string
    @pytest.mark.parametrize("text_content, char_shift", [("abc", 13)])
    def test_should_return_string_when_create_new_string_execute_lowercase(
        self, text_content, char_shift, cipher, mocker
    ):
        mocker.patch(
            "src.ciphers.cipher_rot13.CipherROT13.shift_char",
            side_effect=["n", "o", "p"],
        )
        new_string = cipher.create_new_string(text_content, char_shift)
        assert new_string == "nop"  # nosec

    @pytest.mark.create_new_string
    @pytest.mark.parametrize("text_content, char_shift", [("ABC", 13)])
    def test_should_return_string_when_create_new_string_execute_uppercase(
        self, text_content, char_shift, cipher, mocker
    ):
        mocker.patch(
            "src.ciphers.cipher_rot13.CipherROT13.shift_char",
            side_effect=["N", "O", "P"],
        )
        new_string = cipher.create_new_string(text_content, char_shift)
        assert new_string == "NOP"  # nosec

    @pytest.mark.encrypt
    @pytest.mark.parametrize("text_content", ["abc"])
    def test_should_return_string_when_encrypt_text(self, cipher, mocker, text_content):
        mocker.patch(
            "src.ciphers.cipher_rot13.CipherROT13.create_new_string", return_value="nop"
        )
        decrypted_string = cipher.encrypt(text_content)
        assert decrypted_string == "nop"  # nosec

    @pytest.mark.decrypt
    @pytest.mark.parametrize("text_content", ["abc"])
    def test_should_return_string_when_decrypt_text(self, cipher, mocker, text_content):
        mocker.patch(
            "src.ciphers.cipher_rot13.CipherROT13.create_new_string", return_value="nop"
        )
        decrypted_string = cipher.decrypt(text_content)
        assert decrypted_string == "nop"  # nosec

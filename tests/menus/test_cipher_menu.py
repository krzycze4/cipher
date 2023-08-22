# flake8: noqa E501
import pytest

from src.menus.cipher_menu import CipherMenu


class TestMenu:
    @pytest.fixture()
    def cipher_menu(self):
        return CipherMenu()

    @pytest.mark.display_welcome
    def test_should_check_calls_method_in_display_welcome(self, mocker, cipher_menu):
        mocked_print = mocker.patch("builtins.print")
        cipher_menu.display_welcome()
        expected_calls = [mocker.call("\nWelcome to Cipher")]
        mocked_print.assert_has_calls(expected_calls)
        assert mocked_print.call_count == 1  # nosec

    @pytest.mark.display_main_menu
    def test_should_check_calls_method_in_display_main_manu(self, mocker, cipher_menu):
        mocked_print = mocker.patch("builtins.print")
        cipher_menu.display_main_menu()
        expected_calls = [
            mocker.call("\nMenu:"),
            mocker.call("1. Encrypt texts"),
            mocker.call("2. Decrypt texts"),
            mocker.call("3. Save buffer"),
            mocker.call("4. Load to buffer"),
            mocker.call("5. Exit"),
        ]
        mocked_print.assert_has_calls(expected_calls)
        assert mocked_print.call_count == 6  # nosec

    @pytest.mark.display_main_menu
    def test_should_check_calls_method_in_display_cipher_manu(
        self, mocker, cipher_menu
    ):
        mocked_print = mocker.patch("builtins.print")
        cipher_menu.display_cipher_menu()
        expected_calls = [
            mocker.call("\nChoose cipher:"),
            mocker.call("1. ROT13"),
            mocker.call("2. ROT47"),
        ]
        mocked_print.assert_has_calls(expected_calls)
        assert mocked_print.call_count == 3  # nosec

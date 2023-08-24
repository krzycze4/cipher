import pytest

from src.managers.cipher_manager import CipherManager
from src.menus.cipher_menu import CipherMenu
from src.texts.text import Text


class TestCipherManager:
    def setup_method(self):
        self.manager = CipherManager()

    @pytest.mark.run
    def test_should_do_while_loop_once(self, mocker):
        mocker.patch("src.menus.cipher_menu.CipherMenu.display_welcome")
        mocker.patch("src.menus.cipher_menu.CipherMenu.display_main_menu")
        mocker.patch("src.managers.cipher_manager.CipherManager.take_choice")
        mocker.patch(
            "src.managers.cipher_manager.CipherManager.execute", side_effect=SystemExit
        )
        with pytest.raises(SystemExit):
            self.manager.run()
        assert CipherMenu().display_welcome.call_count == 1
        assert CipherMenu().display_main_menu.call_count == 1
        assert self.manager.take_choice.call_count == 1
        assert self.manager.execute.call_count == 1

    @pytest.mark.run
    def test_should_do_while_loop_twice(self, mocker):
        mocker.patch("src.menus.cipher_menu.CipherMenu.display_welcome")
        mocker.patch("src.menus.cipher_menu.CipherMenu.display_main_menu")
        mocker.patch("src.managers.cipher_manager.CipherManager.take_choice")
        mocker.patch(
            "src.managers.cipher_manager.CipherManager.execute",
            side_effect=[0, SystemExit],
        )
        with pytest.raises(SystemExit):
            self.manager.run()
        assert CipherMenu().display_welcome.call_count == 1
        assert CipherMenu().display_main_menu.call_count == 2
        assert self.manager.take_choice.call_count == 2
        assert self.manager.execute.call_count == 2

    @pytest.mark.take_choice
    def test_should_set_self_choice_when_self_first_out_of_range_then_in_range(
        self, mocker, limit=2
    ):
        mocker.patch("builtins.input", side_effect=[limit + 1, limit])
        self.manager.take_choice(limit=limit)
        assert self.manager.choice == limit

    @pytest.mark.take_choice
    def test_should_set_self_choice_when_self_first_wrong_type_then_correct(
        self, mocker, limit=2
    ):
        mocker.patch("builtins.input", side_effect=["string", limit])
        self.manager.take_choice(limit=limit)
        assert self.manager.choice == limit

    @pytest.mark.execute
    @pytest.mark.parametrize("choice", [1, 2])
    def test_should_call_crypt_text_when_choice_is_1_or_2(self, mocker, choice):
        mocker.patch("src.managers.cipher_manager.CipherManager.crypt_text")
        manager = CipherManager()
        manager.choice = choice
        manager.execute()
        assert manager.crypt_text.call_count == 1

    @pytest.mark.execute
    def test_should_call_save_buffer_when_choice_is_3(self, mocker, choice=3):
        mocker.patch("src.managers.cipher_manager.CipherManager.save_buffer")
        manager = CipherManager()
        manager.choice = choice
        manager.execute()
        assert manager.save_buffer.call_count == 1

    @pytest.mark.execute
    def test_should_call_load_to_buffer_when_choice_is_4(self, mocker, choice=4):
        mocker.patch("src.managers.cipher_manager.CipherManager.load_to_buffer")
        manager = CipherManager()
        manager.choice = choice
        manager.execute()
        assert manager.load_to_buffer.call_count == 1

    @pytest.mark.execute
    def test_should_call_load_to_buffer_when_choice_is_5(self, mocker, choice=5):
        mocker.patch("src.managers.cipher_manager.CipherManager.exit")
        manager = CipherManager()
        manager.choice = choice
        manager.execute()
        assert manager.exit.call_count == 1

    @pytest.mark.exit
    def test_should_count_call_exit_when_exit_execute(self, mocker):
        mocker.patch("builtins.exit")
        manager = CipherManager()
        manager.exit()
        assert exit.call_count == 1

    @pytest.mark.crypt_text
    def test_should_add_crypted_text_to_buffer(self, mocker):
        mocker.patch("copy.copy", return_value=0)
        mocker.patch("src.managers.cipher_manager.CipherManager.take_input_content")
        mocker.patch("src.managers.cipher_manager.CipherManager.encrypt_text")
        mocker.patch("src.menus.cipher_menu.CipherMenu.display_cipher_menu")
        mocker.patch("src.managers.cipher_manager.CipherManager.take_choice")
        manager = CipherManager()
        mocker.patch.object(manager, "status", {0: "ok"})
        mocker.patch.object(manager, "cipher_options", {0: "rot"})
        mocker.patch.object(manager, "crypt_options", {0: manager.encrypt_text})
        manager.choice = 0
        assert manager.buffer.list == []
        manager.crypt_text()
        assert isinstance(manager.buffer.list[0], Text)

    @pytest.mark.take_input_content
    def test_should_set_content_input_when_input_is_not_only_whitespaces(self, mocker):
        mocker.patch("builtins.input", return_value="123")
        self.manager.take_input_content()
        assert self.manager.content_input == "123"

    @pytest.mark.take_input_content
    def test_should_set_content_input_when_input_is_whitespaces_and_then_not(
        self, mocker
    ):
        mocker.patch("builtins.input", side_effect=[" ", "123"])
        self.manager.take_input_content()
        assert self.manager.content_input == "123"

    @pytest.mark.encrypt_text
    def test_should_return_string_when_encrypt_text_execute(self, mocker):
        mocker.patch("src.ciphers.cipher_rot13.CipherROT13.encrypt", return_value="123")
        self.manager.choice = 1
        assert self.manager.encrypt_text() == "123"
        mocker.patch("src.ciphers.cipher_rot47.CipherROT47.encrypt", return_value="123")
        self.manager.choice = 2
        assert self.manager.encrypt_text() == "123"

    @pytest.mark.decrypt_text
    def test_should_return_string_when_decrypt_text_execute(self, mocker):
        mocker.patch("src.ciphers.cipher_rot13.CipherROT13.decrypt", return_value="123")
        self.manager.choice = 1
        assert self.manager.decrypt_text() == "123"
        mocker.patch("src.ciphers.cipher_rot47.CipherROT47.decrypt", return_value="123")
        self.manager.choice = 2
        assert self.manager.decrypt_text() == "123"

    @pytest.mark.save_buffer
    def test_should_clear_buffer_list_when_save_buffer_to_file(self, mocker):
        text = mocker.patch("src.texts.text.Text")
        self.manager.buffer.list = [text, text]
        mocker.patch("src.file_handlers.json_file_handler.JsonFileHandler.save_to_file")
        self.manager.save_buffer()
        assert self.manager.buffer.list == []

    @pytest.mark.load_to_buffer
    def test_should_add_text_objects_to_buffer(self, mocker):
        mocker.patch(
            "src.file_handlers.json_file_handler.JsonFileHandler.load_from_file"
        )
        text = Text(content="123", rot_type="rot", status="ok")
        mocker.patch("src.texts.text.Text.create_from_dict", return_value=text)
        self.manager.file_handler.json_data = [{"1": "1"}, {"2": "2"}]
        self.manager.load_to_buffer()
        assert self.manager.buffer.list == [text, text]

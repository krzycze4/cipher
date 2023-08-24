# flake8: noqa e501
import pytest

from src.file_handlers.json_file_handler import JsonFileHandler


class TestJsonFileHandler:
    def setup_method(self):
        self.json_file_handler = JsonFileHandler()

    @pytest.fixture
    def mocked_correct_json_data(self):
        return [{"content": "abc", "rot_type": "rot13", "status": "encrypted"}]

    @pytest.mark.load_from_file
    def test_should_load_correct_json_data_to_list_from_file(
        self, mocker, mocked_correct_json_data
    ):
        """Checks if loads json file content to json_data when file name is correct or data in json file is correct"""
        mocker.patch("builtins.input", return_value="")
        mocker.patch(
            "builtins.open", mocker.mock_open(read_data=str(mocked_correct_json_data))
        )
        mocker.patch("json.load", return_value=mocked_correct_json_data)
        self.json_file_handler.load_from_file()
        assert self.json_file_handler.json_data == mocked_correct_json_data

    @pytest.mark.load_from_file
    def test_should_load_incorrect_json_data_to_list_from_file(self, mocker):
        """Checks if json_data is [] when file name is incorrect or data in json file is incorrect"""
        mocker.patch("builtins.input", return_value="")
        mocker.patch("builtins.open", side_effect=FileNotFoundError)
        assert self.json_file_handler.json_data is None
        self.json_file_handler.load_from_file()
        assert self.json_file_handler.json_data == []

    @pytest.mark.save_to_file
    def test_should_write_json_data_to_file(self, mocker):
        """Checks if file handler correctly save text data as json data type"""
        mocker.patch(
            "src.file_handlers.json_file_handler.JsonFileHandler.load_from_file",
            return_value=[],
        )
        self.json_file_handler.json_data = []
        text = mocker.patch("src.texts.text.Text")
        buffer_list = [text, text]
        mocker.patch("builtins.open")
        mocker.patch("json.dump")
        text_data = {
            "content": text.content,
            "rot_type": text.rot_type,
            "status": text.status,
        }
        self.json_file_handler.save_to_file(buffer_list)
        assert self.json_file_handler.json_data == [text_data, text_data]

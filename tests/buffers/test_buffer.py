# flake8: noqa: E501
import pytest

from src.buffers.buffer import Buffer


class TestBuffer:
    def setup_method(self):
        self.buffer = Buffer()

    @pytest.fixture
    def mocked_text(self, mocker):
        return mocker.patch("src.texts.text.Text")

    @pytest.mark.add
    def test_should_check_len_list_when_add_once_to_empty_list(self, mocked_text):
        len_before_add = len(self.buffer.list)
        self.buffer.add(mocked_text)
        assert len_before_add + 1 == len(self.buffer.list)

    @pytest.mark.add
    def test_should_check_len_list_when_add_twice_to_empty_list(self, mocked_text):
        len_before_add = len(self.buffer.list)
        self.buffer.add(mocked_text)
        self.buffer.add(mocked_text)
        assert len_before_add + 2 == len(self.buffer.list)

    @pytest.mark.add
    def test_should_check_len_list_when_add_to_not_empty_list(self, mocked_text):
        self.buffer.list = [mocked_text, mocked_text]
        len_before_add = len(self.buffer.list)
        self.buffer.add(mocked_text)
        assert len_before_add + 1 == len(self.buffer.list)

    @pytest.mark.clear
    def test_should_check_len_list_when_clear_empty_list(self):
        len_before_clear = len(self.buffer.list)
        self.buffer.clear()
        assert len_before_clear == len(self.buffer.list)

    @pytest.mark.clear
    def test_should_check_len_list_when_clear_not_empty_list(self, mocked_text):
        self.buffer.list = [mocked_text, mocked_text]
        len_before_clear = len(self.buffer.list)
        self.buffer.clear()
        assert len_before_clear - 2 == len(self.buffer.list)

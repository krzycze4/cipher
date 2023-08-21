# flake8: noqa: E501
import pytest

from src.buffers.buffer import Buffer


class TestBuffer:
    @pytest.fixture
    def buffer(self):
        return Buffer()

    @pytest.fixture
    def mocked_text(self, mocker):
        return mocker.patch("src.texts.text.Text")

    @pytest.mark.add
    def test_should_check_len_list_when_add_once_to_empty_list(
        self, buffer, mocked_text
    ):
        len_before_add = len(buffer.list)
        buffer.add(mocked_text)
        assert len_before_add + 1 == len(buffer.list)  # nosec

    @pytest.mark.add
    def test_should_check_len_list_when_add_twice_to_empty_list(
        self, buffer, mocked_text
    ):
        len_before_add = len(buffer.list)
        buffer.add(mocked_text)
        buffer.add(mocked_text)
        assert len_before_add + 2 == len(buffer.list)  # nosec

    @pytest.mark.add
    def test_should_check_len_list_when_add_to_not_empty_list(
        self, buffer, mocked_text
    ):
        buffer.list = [mocked_text, mocked_text]
        len_before_add = len(buffer.list)
        buffer.add(mocked_text)
        assert len_before_add + 1 == len(buffer.list)  # nosec

    @pytest.mark.clear
    def test_should_check_len_list_when_clear_empty_list(self, buffer):
        len_before_clear = len(buffer.list)
        buffer.clear()
        assert len_before_clear == len(buffer.list)  # nosec

    @pytest.mark.clear
    def test_should_check_len_list_when_clear_not_empty_list(self, buffer, mocked_text):
        buffer.list = [mocked_text, mocked_text]
        len_before_clear = len(buffer.list)
        buffer.clear()
        assert len_before_clear - 2 == len(buffer.list)  # nosec

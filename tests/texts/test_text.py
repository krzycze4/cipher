from src.texts.text import Text


class TestText:
    def test_should_return_text_object(self):
        """Check if method correctly create new Text object from dictionary"""
        text_data = {"content": "1", "rot_type": "rot", "status": "ok"}
        text = Text.create_from_dict(text_data)
        assert isinstance(text, Text)
        assert text.content == "1"
        assert text.rot_type == "rot"
        assert text.status == "ok"

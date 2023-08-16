from typing import List

from src.texts.text import Text


class Buffer:
    def __init__(self):
        self.list: List[Text] = []

    def add(self, text: Text):
        self.list.append(text)

    def clear(self):
        self.list.clear()

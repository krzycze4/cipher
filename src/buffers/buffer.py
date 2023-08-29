"""Module represents class Buffer"""
from typing import List

from texts.text import Text


class Buffer:
    def __init__(self):
        self.list: List[Text] = []

    def add(self, text: Text):
        """Method adds a new object Text to the list"""
        self.list.append(text)

    def clear(self):
        """Method clears the whole list"""
        self.list.clear()

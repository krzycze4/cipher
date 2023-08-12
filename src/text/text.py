from dataclasses import dataclass
from typing import Union


@dataclass
class Text:
    _content: Union[None, str] = None
    _rot_type: Union[None, str] = None
    _status: Union[None, str] = None

    @property
    def content(self):
        return self._content

    @property
    def rot_type(self):
        return self._rot_type

    @property
    def status(self):
        return self._status

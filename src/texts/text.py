"""
A module to represent a dataclass of Text.

Classes:
    Text
"""
from dataclasses import dataclass
from typing import Union


@dataclass
class Text:
    """
    A class to represent a cipher ROT13.

    Parameters
    __________
    _content: Union[None, str] = None
    _rot_type: Union[None, str] = None
    _status: Union[None, str] = None

    Methods
    _______
    content() -> str
        returns self._content
    rot_type() -> str
        returns self._rot_type
    status() -> str
        returns self._status
    """
    _content: Union[None, str] = None
    _rot_type: Union[None, str] = None
    _status: Union[None, str] = None

    @property
    def content(self) -> str:
        """
        A method returns self._content.

        Returns
        _______
        self._content: str
        """
        return self._content

    @property
    def rot_type(self) -> str:
        """
        A method returns self._rot_type.

        Returns
        _______
        self._rot_type: str
        """
        return self._rot_type

    @property
    def status(self) -> str:
        """
        A method returns self._status.

        Returns
        _______
        self._status: str
        """
        return self._status

from dataclasses import dataclass
from typing import Union


@dataclass
class Text:
    _content: Union[None, str] = None
    _rot_type: Union[None, str] = None
    _status: Union[None, str] = None

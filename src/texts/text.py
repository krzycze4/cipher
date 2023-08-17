"""A module to represent a dataclass Text."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class Text:
    content: str
    rot_type: str
    status: str

    @classmethod
    def create_from_dict(cls, text_data: Dict[str, str]) -> Text:
        """Method creates Text object from dict
        Parameters:
            text_data: Dict[str, str]
                3 key-values pairs with keys: content, rot_type, status
        """
        content = text_data.get("content")
        rot_type = text_data.get("rot_type")
        status = text_data.get("status")
        return cls(content=content, rot_type=rot_type, status=status)

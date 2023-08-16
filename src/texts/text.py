"""A module to represent a dataclass Text."""
from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class Text:
    content: str
    rot_type: str
    status: str

    @classmethod
    def create_from_dict(cls, text_data: Dict) -> object:
        content = text_data.get("content")
        rot_type = text_data.get("rot_type")
        status = text_data.get("status")
        return cls(content=content, rot_type=rot_type, status=status)

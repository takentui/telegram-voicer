from typing import Optional

from pydantic import BaseModel


class MediaFile(BaseModel):
    file_id: int
    duration: float
    path: str
    name: Optional[str]

    def __eq__(self, other: 'MediaFile') -> bool:
        return self.file_id == other.file_id

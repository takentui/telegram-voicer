from typing import Optional

from pydantic import BaseModel


class CreateMediaFileModel(BaseModel):
    duration: float
    path: str
    name: Optional[str]

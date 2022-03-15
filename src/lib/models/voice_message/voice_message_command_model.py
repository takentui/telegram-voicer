from typing import Optional

from pydantic import BaseModel


class CreateVoiceMessageModel(BaseModel):
    file_id: int
    duration: float


class UpdateVoiceMessageModel(BaseModel):
    message_id: int
    duration: Optional[float]

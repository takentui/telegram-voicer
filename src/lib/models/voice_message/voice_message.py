from pydantic import BaseModel


class VoiceMessage(BaseModel):
    message_id: int
    file_id: int
    duration: float

    def __eq__(self, other: 'VoiceMessage') -> bool:
        return self.message_id == other.message_id

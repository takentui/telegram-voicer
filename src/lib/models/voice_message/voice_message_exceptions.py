from pydantic import Field, BaseModel


class VoiceMessageNotFoundError(Exception):
    message = "Voice message not found"

    def __str__(self):
        return VoiceMessageNotFoundError.message


class ErrorMessageVoiceMessageNotFound(BaseModel):
    detail: str = Field(example=VoiceMessageNotFoundError.message)

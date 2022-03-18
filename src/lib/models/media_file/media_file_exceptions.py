from pydantic import Field, BaseModel


class MediaFileNotFoundError(Exception):
    message = "Media file not found"

    def __str__(self):
        return MediaFileNotFoundError.message


class ErrorMessageMediaFileNotFound(BaseModel):
    detail: str = Field(example=MediaFileNotFoundError.message)

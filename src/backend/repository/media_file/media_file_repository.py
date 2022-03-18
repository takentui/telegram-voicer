from sqlalchemy.orm import Session

from lib.models.media_file import MediaFile, CreateMediaFileModel
from .abstract_repository import AbstractMediaFileRepository


class MediaFileRepositoryAlchemy(AbstractMediaFileRepository):
    _session: Session

    def __init__(self, session: Session, *args, **kwargs):
        self._session = session
        super().__init__(*args, **kwargs)

    async def read(self, file_id: int) -> MediaFile:
        pass

    async def create(self, create_model: CreateMediaFileModel) -> MediaFile:
        pass

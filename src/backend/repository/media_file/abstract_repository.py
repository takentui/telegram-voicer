import logging
from abc import ABC, abstractmethod
from typing import Optional

from lib.models.media_file import MediaFile, CreateMediaFileModel


class AbstractMediaFileRepository(ABC):
    _logger: logging.Logger

    def __init__(self, logger: Optional[logging.Logger] = None):
        self._logger = logger

    @abstractmethod
    async def read(self, file_id: int) -> MediaFile:
        pass

    @abstractmethod
    async def create(self, create_model: CreateMediaFileModel) -> MediaFile:
        pass

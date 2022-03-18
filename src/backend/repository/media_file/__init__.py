import logging

from sqlalchemy.orm import Session

from .abstract_repository import AbstractMediaFileRepository
from .media_file_repository import MediaFileRepositoryAlchemy


# TODO: Create an honest factory, get rid of the session object
def media_file_repository_factory(session: Session, logger: logging.Logger) -> AbstractMediaFileRepository:
    return MediaFileRepositoryAlchemy(session, logger)


__all__ = [
    'AbstractMediaFileRepository',
    'media_file_repository_factory'
]

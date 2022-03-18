import logging

from sqlalchemy.orm import Session

from .abstract_repository import AbstractVoiceMessageRepository
from .voice_message_repository import VoiceMessageRepositoryAlchemy


# TODO: Create an honest factory, get rid of the session object
def voice_message_repository_factory(session: Session, logger: logging.Logger) -> AbstractVoiceMessageRepository:
    return VoiceMessageRepositoryAlchemy(session, logger)


__all__ = [
    'AbstractVoiceMessageRepository',
    'voice_message_repository_factory'
]

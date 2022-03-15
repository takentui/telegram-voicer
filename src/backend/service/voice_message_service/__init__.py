import logging

from backend.repository.voice_message import AbstractVoiceMessageRepository
from .abstract_voice_message_service import AbstractVoiceMessageService
from .voice_message_service import VoiceMessageServiceImpl


def voice_message_service_factory(repo: AbstractVoiceMessageRepository, logger: logging.Logger) -> AbstractVoiceMessageService:
    return VoiceMessageServiceImpl(repo=repo, logger=logger)


__all__ = [
    'voice_message_service_factory',
    'AbstractVoiceMessageService'
]

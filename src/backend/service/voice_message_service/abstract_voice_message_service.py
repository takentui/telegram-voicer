import logging
from abc import ABC, abstractmethod
from typing import Optional

from lib.models.voice_message import (
    VoiceMessage,
    CreateVoiceMessageModel,
    UpdateVoiceMessageModel
)


class AbstractVoiceMessageService(ABC):
    _logger: logging.Logger

    def __init__(self, logger: Optional[logging.Logger] = None):
        self._logger = logger

    @abstractmethod
    async def create(self, create_model: CreateVoiceMessageModel) -> VoiceMessage:
        pass

    @abstractmethod
    async def read(self, message_id: int) -> VoiceMessage:
        pass

    @abstractmethod
    async def update(self, update_model: UpdateVoiceMessageModel) -> VoiceMessage:
        pass

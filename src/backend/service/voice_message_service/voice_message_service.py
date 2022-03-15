from backend.repository.voice_message import AbstractVoiceMessageRepository
from backend.service.voice_message_service import AbstractVoiceMessageService
from lib.models.voice_message import (
    UpdateVoiceMessageModel,
    VoiceMessage,
    CreateVoiceMessageModel
)


class VoiceMessageServiceImpl(AbstractVoiceMessageService):
    _repo: AbstractVoiceMessageRepository

    def __init__(self, repo: AbstractVoiceMessageRepository, *args, **kwargs):
        self._repo = repo
        super().__init__(*args, **kwargs)

    async def create(self, create_model: CreateVoiceMessageModel) -> VoiceMessage:
        pass

    async def read(self, message_id: int) -> VoiceMessage:
        pass

    async def update(self, update_model: UpdateVoiceMessageModel) -> VoiceMessage:
        pass

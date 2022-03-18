from sqlalchemy.orm import Session

from backend.repository.voice_message import AbstractVoiceMessageRepository
from lib.models.voice_message import CreateVoiceMessageModel, VoiceMessage


class VoiceMessageRepositoryAlchemy(AbstractVoiceMessageRepository):
    _session: Session

    def __init__(self, session: Session, *args, **kwargs):
        self._session = session
        super().__init__(*args, **kwargs)

    async def read(self, message_id: int) -> VoiceMessage:
        pass

    async def create(self, create_model: CreateVoiceMessageModel) -> VoiceMessage:
        pass

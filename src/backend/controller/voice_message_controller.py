import logging
from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from backend.repository.database import get_session
from backend.repository.voice_message import AbstractVoiceMessageRepository, voice_message_repository_factory
from backend.service.voice_message_service import AbstractVoiceMessageService
from backend.service.voice_message_service import voice_message_service_factory
from lib.models.voice_message import VoiceMessage, ErrorMessageVoiceMessageNotFound

router = APIRouter()
logger = logging.getLogger('VOICE_MESSAGE')


def build_voice_message_repository(session: Session = Depends(get_session)) -> AbstractVoiceMessageRepository:
    return voice_message_repository_factory(session, logger)


def build_voice_message_service(
        repo: AbstractVoiceMessageRepository = Depends(build_voice_message_repository)) -> AbstractVoiceMessageService:
    return voice_message_service_factory(repo, logger)


@router.get('/voice_message/{voice_message_id}',
            response_model=VoiceMessage,
            status_code=status.HTTP_200_OK,
            responses={
                status.HTTP_404_NOT_FOUND: {
                    "model": ErrorMessageVoiceMessageNotFound,
                },
            },
            )
async def get_voice_message(voice_message_id: int,
                            voice_message_service: AbstractVoiceMessageService = Depends(build_voice_message_service)):
    return voice_message_service.read(voice_message_id)

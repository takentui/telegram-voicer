import logging
from logging import config
from typing import Optional

import uvicorn as uvicorn
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.repository.database import get_session
from backend.repository.voice_message import AbstractVoiceMessageRepository, voice_message_repository_factory
from backend.service.voice_message_service import AbstractVoiceMessageService, voice_message_service_factory

config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)


class ApplicationConfiguration(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8080


class ApplicationBuilder:
    _config: ApplicationConfiguration
    _app: Optional[FastAPI] = None

    def __init__(self, app_config: ApplicationConfiguration):
        self._config = app_config

    def build_application(self):
        self._app = FastAPI(title="Telegram Voicer")

    def run(self):
        if self._app is not None:
            uvicorn.run(self._app, host=self._config.host, port=self._config.port)
        else:
            raise ValueError('Application not created! Please build them!')


def build_voice_message_repository(session: Session = Depends(get_session),
                                   logger_instance: Optional[
                                       logging.Logger] = logger) -> AbstractVoiceMessageRepository:
    return voice_message_repository_factory(session, logger_instance)


def build_voice_message_service(
        repo: AbstractVoiceMessageRepository = Depends(build_voice_message_repository),
        logger_instance: Optional[logging.Logger] = logger) -> AbstractVoiceMessageService:
    return voice_message_service_factory(repo, logger_instance)

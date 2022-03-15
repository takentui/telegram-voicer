import logging
from logging import config
from typing import Iterator, Optional

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from backend.repository.database import create_tables, SessionLocal
from backend.repository.voice_message import AbstractVoiceMessageRepository, voice_message_repository_factory
from backend.service.voice_message_service import AbstractVoiceMessageService, voice_message_service_factory

config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app = FastAPI()

create_tables()


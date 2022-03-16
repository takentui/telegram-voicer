import logging
import os.path
from logging import config
from typing import Optional

import uvicorn as uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base

from backend.controller import router

if os.path.exists("logging.conf"):
    config.fileConfig("logging.conf", disable_existing_loggers=False)

logger = logging.getLogger(__name__)


class ApplicationConfiguration(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8080
    dsn: str = "sqlite:///./db/sqlite.db"
    make_db: bool = True


class ApplicationBuilder:
    _config: ApplicationConfiguration
    _app: Optional[FastAPI] = None
    _engine: Engine

    def __init__(self, app_config: ApplicationConfiguration):
        self._config = app_config
        self._init_db()

    def _init_db(self):
        self._engine = create_engine(
            self._config.dsn,
            connect_args={
                "check_same_thread": False,
            },
        )

        if self._config.make_db:
            base = declarative_base()
            base.metadata.create_all(bind=self._engine)

    def _register_api_routers(self):
        self._app.include_router(router)

    def initialize(self):
        self._app = FastAPI(title="Telegram Voicer")
        self._register_api_routers()

    def run(self):
        if self._app is not None:
            uvicorn.run(self._app, host=self._config.host, port=self._config.port)
        else:
            raise ValueError('Application not created! Please build them!')

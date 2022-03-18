from fastapi import APIRouter, Depends

from .voice_message_controller import router as voice_message_router, build_voice_message_service

router = APIRouter()
router.include_router(voice_message_router, dependencies=[Depends(build_voice_message_service)])

__all__ = [
    'router'
]

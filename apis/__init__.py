from fastapi import APIRouter
from .chat.router import chat_router

root_api_router = APIRouter()
root_api_router.include_router(chat_router)

__all__ = ["root_api_router"]

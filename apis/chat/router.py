from fastapi import APIRouter, Request
from .schema import ChatRequest, ChatResponse

chat_router = APIRouter()

@chat_router.post('/question', response_model=ChatResponse, status_code=200)
async def question(request:Request, body: ChatRequest):
    """
    just ask question
    """
    qa_model = request.scope['app'].qa_ml_model
    answer = qa_model.run(body.question)
    return {'answer': answer}

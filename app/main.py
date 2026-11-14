from typing import Annotated, Any

from fastapi import Depends, FastAPI, status

from app.config import Settings, get_settings
from app.schemas import ChatRequest, ChatResponse
from app.services.inference import generate_mock_chat

app = FastAPI(
    title="Tensoy API",
    description="API for prompt response and emotion state inference.",
    version="0.1.0",
)


@app.get(
    "/health",
    status_code=status.HTTP_200_OK,
    summary="Health Check",
    response_model=dict[str, Any],
)
def health_check(
    settings: Annotated[Settings, Depends(get_settings)],
) -> dict[str, Any]:
    return {
        "status": "ok",
        "mock_mode": settings.mock_mode,
        "environment": settings.environment,
    }


@app.post(
    "/chat",
    status_code=status.HTTP_200_OK,
    summary="Prompt Response with Emotional Emoji",
    response_model=ChatResponse,
)
def chat_endpoint(
    request: ChatRequest,
    settings: Annotated[Settings, Depends(get_settings)],
) -> ChatResponse:
    if settings.mock_mode:
        response_text, emoji_char = generate_mock_chat(request.prompt)
    else:
        # Fallback/placeholder for real inference provider when mock_mode is disabled
        response_text, emoji_char = generate_mock_chat(request.prompt)

    return ChatResponse(response=response_text, emoji=emoji_char)

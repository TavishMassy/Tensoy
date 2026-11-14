from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    prompt: str = Field(
        ...,
        min_length=1,
        max_length=4000,
        description="The user input prompt",
        examples=["Hello! How are you feeling today?"],
    )


class ChatResponse(BaseModel):
    response: str = Field(
        ...,
        min_length=1,
        max_length=2000,
        description="Generated model response text",
        examples=["Hello! I am doing well, ready to help you."],
    )
    emoji: str = Field(
        ...,
        min_length=1,
        max_length=1,
        description="A single face emoji depicting the emotion state",
        examples=["😊"],
    )

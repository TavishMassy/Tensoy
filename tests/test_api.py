from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["mock_mode"] is True


def test_chat_mock_greeting() -> None:
    payload = {"prompt": "Hello there!"}
    response = client.post("/chat", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert "emoji" in data
    assert len(data["emoji"]) == 1
    assert data["emoji"] == "😊"
    assert len(data["response"]) <= 2000


def test_chat_mock_question() -> None:
    payload = {"prompt": "How does this system function?"}
    response = client.post("/chat", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["emoji"] == "🤔"
    assert len(data["emoji"]) == 1


def test_chat_mock_celebration() -> None:
    payload = {"prompt": "We achieved a great milestone today!"}
    response = client.post("/chat", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["emoji"] == "🥳"
    assert len(data["emoji"]) == 1


def test_chat_mock_idea() -> None:
    payload = {"prompt": "I want to create a new solution"}
    response = client.post("/chat", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["emoji"] == "🧐"
    assert len(data["emoji"]) == 1


def test_chat_mock_fallback() -> None:
    payload = {"prompt": "Random unstructured test phrase"}
    response = client.post("/chat", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["emoji"] == "😐"
    assert len(data["emoji"]) == 1


def test_chat_validation_empty_prompt() -> None:
    payload = {"prompt": ""}
    response = client.post("/chat", json=payload)
    assert response.status_code == 422


def test_chat_validation_missing_prompt() -> None:
    payload = {}
    response = client.post("/chat", json=payload)
    assert response.status_code == 422


def test_chat_validation_oversized_prompt() -> None:
    payload = {"prompt": "a" * 4001}
    response = client.post("/chat", json=payload)
    assert response.status_code == 422

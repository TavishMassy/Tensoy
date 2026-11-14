# Tensoy API

A decoupled, asynchronous FastAPI microservice providing prompt responses with deterministic emotion states and single face emojis in mock mode.

Built following strict architecture boundaries, deterministic sensors, and containerized deployment.

---

## Architecture Overview

```mermaid
flowchart LR
    Client["Client / curl / Frontend"] -->|POST /chat| API["app/main.py (FastAPI)"]
    API -->|Validate Contract| Schemas["app/schemas.py (Pydantic)"]
    API -->|Load Config| Config["app/config.py (pydantic-settings)"]
    API -->|Delegate Logic| Service["app/services/inference.py"]
    Service -->|Deterministic Mock Inference| API
    API -->|JSON (response + face emoji)| Client
```

- **`app/schemas.py`**: API request/response contracts strictly decoupled from business logic.
- **`app/config.py`**: Environment and runtime configuration managed via `pydantic-settings`.
- **`app/services/inference.py`**: Business logic handling mock emotion detection and deterministic response generation.
- **`app/main.py`**: FastAPI route definitions, lifespan, and dependency injection.
- **`tests/test_api.py`**: Automated test suite verifying health, mock responses, character limits, face emoji constraints, and schema validations.

---

## API Specification

### 1. Health Check
- **Endpoint**: `GET /health`
- **Response**:
```json
{
  "status": "ok",
  "mock_mode": true,
  "environment": "development"
}
```

### 2. Chat Inference (Mock Mode)
- **Endpoint**: `POST /chat`
- **Request Body**:
```json
{
  "prompt": "Hello there! How are you?"
}
```
  - `prompt`: String (minimum 1 character, maximum 4,000 characters).

- **Response Body**:
```json
{
  "response": "Hello! It's great to hear from you. How can I assist you today?",
  "emoji": "😊"
}
```
  - `response`: String (minimum 1 character, maximum 2,000 characters).
  - `emoji`: String (strictly **1 character**, restricted exclusively to **face emojis**).

#### Face Emoji Mapping in Mock Mode
| Prompt Trigger / Sentiment | Face Emoji | Unicode / Name |
| :--- | :---: | :--- |
| Greetings (`hello`, `hi`, `hey`) | `😊` | Smiling face with smiling eyes |
| Inquiries / Questions (`what`, `why`, `how`, `?`) | `🤔` | Thinking face |
| Achievements / Milestones (`great`, `awesome`, `win`) | `🥳` | Partying face |
| Ideas / Problem-solving (`idea`, `create`, `solve`) | `🧐` | Face with monocle |
| General / Fallback | `😐` | Neutral face |

---

## Getting Started with Docker

### Prerequisites
- Docker & Docker Compose (or Docker Desktop on Windows/macOS)

### 1-Click Startup & Shutdown Scripts

#### On Linux / macOS / Git Bash / WSL:
The scripts enforce strict shell safety (`set -euo pipefail`):
```bash
# Start service and run test sensors
chmod +x start.sh stop.sh
./start.sh

# Stop service
./stop.sh
```

#### On Windows (PowerShell):
```powershell
# Start service and run test sensors
.\start.ps1

# Stop service
.\stop.ps1
```

Both scripts automatically:
1. Build the Docker container.
2. Launch the service in the background (`docker compose up --build -d`).
3. Run the automated `pytest` sensor suite inside the container.
4. Expose the API at `http://localhost:8000`.

---

## Manual Docker Commands

### Build & Run
```bash
# Build the Docker image
docker compose build

# Start the service
docker compose up -d

# View live logs
docker compose logs -f tensoy

# Stop the service
docker compose down
```

### Run Sensors (Tests, Lint, Type Check)
All tests and code quality sensors run cleanly inside the Linux container:

```bash
# Run test suite
docker compose run --rm tensoy pytest -v

# Run Ruff linter
docker compose run --rm tensoy ruff check .

# Run Mypy static type checker
docker compose run --rm tensoy mypy app/
```

---

## Interactive Documentation
Once started, view the interactive OpenAPI documentation:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

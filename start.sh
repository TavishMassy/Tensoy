#!/usr/bin/env bash
set -euo pipefail

echo "========================================"
echo " Starting Tensoy API with Docker Compose"
echo "========================================"

if ! command -v docker > /dev/null 2>&1; then
    echo "Error: docker is not installed or not in PATH." >&2
    exit 1
fi

echo "Building and launching container..."
docker compose up --build -d

echo "Waiting for service initialization..."
sleep 3

echo "Running verification sensor suite in container..."
docker compose exec -T tensoy pytest -v

echo ""
echo "========================================"
echo " Tensoy API is ready!"
echo " Health: http://localhost:8000/health"
echo " Docs:   http://localhost:8000/docs"
echo " Logs:   docker compose logs -f tensoy"
echo "========================================"

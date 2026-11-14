#!/usr/bin/env bash
set -euo pipefail

echo "========================================"
echo " Stopping Tensoy API Docker Services"
echo "========================================"

if ! command -v docker > /dev/null 2>&1; then
    echo "Error: docker is not installed or not in PATH." >&2
    exit 1
fi

echo "Stopping containers..."
docker compose down

echo "Tensoy API services have been stopped."

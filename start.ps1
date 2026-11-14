# PowerShell startup script for Tensoy API
$ErrorActionPreference = "Stop"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host " Starting Tensoy API with Docker Compose" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    Write-Error "Error: docker CLI is not installed or not in PATH."
    exit 1
}

Write-Host "Building and launching container..." -ForegroundColor Green
docker compose up --build -d

Write-Host "Waiting for service initialization..." -ForegroundColor Yellow
Start-Sleep -Seconds 3

Write-Host "Running verification sensor suite in container..." -ForegroundColor Green
docker compose exec -T tensoy pytest -v

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host " Tensoy API is ready!" -ForegroundColor Green
Write-Host " Health: http://localhost:8000/health" -ForegroundColor White
Write-Host " Docs:   http://localhost:8000/docs" -ForegroundColor White
Write-Host " Logs:   docker compose logs -f tensoy" -ForegroundColor White
Write-Host "========================================" -ForegroundColor Cyan

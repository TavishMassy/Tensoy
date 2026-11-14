# PowerShell shutdown script for Tensoy API
$ErrorActionPreference = "Stop"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host " Stopping Tensoy API Docker Services" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    Write-Error "Error: docker CLI is not installed or not in PATH."
    exit 1
}

Write-Host "Stopping containers..." -ForegroundColor Yellow
docker compose down

Write-Host "Tensoy API services have been stopped." -ForegroundColor Green

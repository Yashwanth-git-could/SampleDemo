# FastAPI Cloud Run Application

A simple FastAPI application with automated CI/CD deployment to Google Cloud Run.

## Features

- FastAPI web framework
- Automatic deployment on push to `main` branch
- Containerized with Docker
- Deployed on Google Cloud Run

## API Endpoints

- `GET /` - Root endpoint (returns calculation result)
- `GET /health` - Health check endpoint
- `GET /items/{item_id}` - Get item by ID with optional query parameter

## Local Development

### Prerequisites
- Python 3.11+
- Docker (optional)

### Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
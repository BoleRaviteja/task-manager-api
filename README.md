# Task Manager API

A Python project for learning backend development, REST APIs, and QA automation.

## Technologies
- Python
- FastAPI
- Uvicorn
- pytest
- HTTPX

## Setup

Install dependencies using:

    python -m pip install -r requirements.txt

## Run the application

    python -m uvicorn app.main:app --reload

## API documentation

http://127.0.0.1:8000/docs

## Run tests

    python -m pytest -v

## Status
Under development.

## Running with Docker

### Prerequisites

- Docker Desktop installed and running
- Docker Compose available through the Docker CLI

### Start the API

From the project root, run:

```bash
docker compose up --build -d
```

This builds the Docker image and starts the API in the background.

The API will be available at:

- API documentation: http://localhost:8000/docs
- Health check: http://localhost:8000/health

### View logs

```bash
docker compose logs -f api
```

Press `Ctrl+C` to stop following the logs. This does not stop the container.

### Check container status

```bash
docker compose ps
```

### Stop the API

```bash
docker compose down
```

This stops and removes the Compose container and network. The named database volume is preserved.

### Database persistence

Docker Compose uses the named volume `task_data` to store the SQLite database at `/data/tasks.db` inside the container.

The database persists when the container is restarted or recreated using normal Compose commands.

**Warning:** The following command deletes the Compose-managed volume, including its persisted database:

```bash
docker compose down -v
```

Only use `-v` when you intentionally want to remove the persisted database data.

### Rebuild after code changes

```bash
docker compose up --build -d
```

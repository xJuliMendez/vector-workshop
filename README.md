# Vector Database Workshop

This workshop demonstrates how to implement and use vector databases in a Symfony application with a separate Python embedding service.

## Architecture

The project consists of three main components:
- Symfony API (Main application)
- Python Embedding Service (Vector embedding generation)
- PostgreSQL with pgvector (Vector storage)

## Prerequisites

- Docker
- Docker Compose
- Make (optional, but recommended)

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd vector-workshop
```

2. Build and start the containers:
```bash
make setup
```

3. Access the services:
- Symfony API: http://localhost:8000
- Embedding API: http://localhost:8001
- PostgreSQL: localhost:5432

## Project Structure

- `symfony-api/`: Symfony application following Clean Architecture
- `embedding-api/`: Python FastAPI application for generating embeddings
- `docker/`: Docker configuration files 
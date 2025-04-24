.PHONY: up down build logs ps shell-php shell-python shell-db

# Docker compose commands
up:
	docker-compose up -d

down:
	docker-compose down

build:
	docker-compose build

logs:
	docker-compose logs -f

ps:
	docker-compose ps

# Shell access
shell-php:
	docker-compose exec symfony-api bash

shell-python:
	docker-compose exec embedding-api bash

shell-db:
	docker-compose exec vector-db psql -U vector_user -d vector_db

# Initial setup
setup: build up
	docker-compose exec symfony-api composer create-project symfony/skeleton .
	docker-compose exec embedding-api pip install -r requirements.txt

# Clean
clean:
	docker-compose down -v 
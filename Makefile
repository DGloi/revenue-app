# Makefile for Local Development

# Define environment variables for local development
export POSTGRES_DB=reviewdb
export POSTGRES_USER=admin
export POSTGRES_PASSWORD=password
export DATABASE_URL=postgres://admin:password@db:5432/reviewdb
export ALLOWED_HOSTS=localhost

.PHONY: all setup build up down logs

# Default target, runs setup and up
all: setup build up

# Setup dependencies (Docker, Docker Compose)
setup:
	@echo "Checking for Docker..."
	@docker --version || (echo "Docker is not installed. Please install Docker." && exit 1)
	@echo "Checking for Docker Compose..."
	@docker-compose --version || (echo "Docker Compose is not installed. Please install Docker Compose." && exit 1)
	@echo "All dependencies are installed."

# Build all Docker images
build:
	docker-compose build --no-cache

# Start all services
up:
	docker-compose up -d

# Stop all services
down:
	docker-compose down

# Run backend tests
backend-test:
	docker-compose run --rm backend-tests

# Run frontend tests
frontend-test:
	docker-compose run --rm frontend-tests

# Run all tests
test: backend-test frontend-test

# View logs for all services
logs:
	docker-compose logs -f
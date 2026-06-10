# Day 26 - Flask and Redis with Docker Compose

## Objective

Learn how multiple containers communicate using Docker Compose.

## Services

### Web Service

* Flask Application
* Runs on port 5000 inside container
* Exposed on localhost:5002

### Redis Service

* Redis Cache
* Stores visit count

## Project Structure

* app.py
* requirements.txt
* Dockerfile
* docker-compose.yml
* README.md

## What I Learned

* Multi-container applications
* Service-to-service communication
* Docker Compose networking
* Redis integration with Flask
* Container dependency management

## Commands Used

```bash
docker compose up -d

docker compose ps

docker ps

docker compose down
```

## Result

Successfully deployed Flask and Redis containers using Docker Compose.

Application URL:

http://localhost:5002

The visit counter increased on every page refresh, proving communication between Flask and Redis.

## Key Takeaway

Docker Compose makes it easy to run and connect multiple services as a single application.

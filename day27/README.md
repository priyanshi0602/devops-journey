# Day 27 - Nginx Reverse Proxy with Flask

## Objective

Learn how Nginx works as a reverse proxy in front of a Flask application using Docker Compose.

## Architecture

Browser
↓
Nginx
↓
Flask Application

## Project Structure

* app.py
* requirements.txt
* Dockerfile
* docker-compose.yml
* nginx.conf
* README.md

## What I Learned

* Nginx reverse proxy
* Docker Compose multi-container setup
* Container communication
* Request forwarding
* Production-style application architecture

## Commands Used

```bash
docker compose up -d

docker compose ps

docker ps

docker compose down
```

## Result

Successfully deployed Nginx and Flask containers.

Application URL:

http://localhost:8085

Output:

Hello from Day 27 - Nginx Reverse Proxy!

## Key Takeaway

Nginx can act as a reverse proxy, forwarding requests to backend applications such as Flask while providing a production-ready architecture.

# Day 31 - Multi-Service Application Architecture

## Objective

Learn how Docker Compose can manage multiple services together.

## Services Used

* Nginx
* PostgreSQL
* Redis

## Commands

Start Services:

docker compose up -d

Check Running Services:

docker compose ps

View Logs:

docker logs day31-postgres-1
docker logs day31-redis-1

## Outcome

Successfully deployed a multi-container environment using Docker Compose.

Verified:

* PostgreSQL was ready to accept connections.
* Redis was ready to accept connections.
* Nginx was running successfully.

This setup represents the foundation of a real-world application architecture where different services work together inside a Docker environment.

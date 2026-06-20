# Day 35 – Docker Compose Multi-Container Application

## What I Learned

- Docker Compose
- Running multiple containers together
- PostgreSQL container
- Redis container
- Nginx container
- Container networking
- Container management with Compose

## Commands Used

docker compose up -d

docker compose ps

docker logs <container>

docker exec -it <container> redis-cli

docker exec -it <container> psql -U admin -d appdb

docker compose down

## Outcome

Successfully deployed and managed a multi-container application stack using Docker Compose.
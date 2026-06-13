# Day 29 - PostgreSQL with Docker Compose

## Objective

Learn how to deploy and manage a PostgreSQL database using Docker Compose.

## Services

### PostgreSQL

* PostgreSQL 15
* Port 5432
* Database: devopsdb
* User: admin

## Project Structure

* docker-compose.yml
* README.md

## What I Learned

* PostgreSQL basics
* Running databases in containers
* Docker Compose services
* Database initialization
* Containerized database management

## Commands Used

docker compose up -d

docker compose ps

docker ps

docker logs

docker exec -it day29-postgres-1 psql -U admin -d devopsdb

## Result

Successfully deployed PostgreSQL using Docker Compose and verified database startup.

## Key Takeaway

Databases can be deployed and managed consistently using Docker containers and Docker Compose.

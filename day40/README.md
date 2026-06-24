# Day 40 - Multi-Tier Docker Architecture

## Objective

Understand communication between multiple containers using Docker Networking.

## Architecture

Nginx Container → PostgreSQL Container

## Commands Used

docker network create day40-network

docker run -d --name day40-postgres --network day40-network postgres:15

docker run -d --name day40-nginx --network day40-network nginx

docker network inspect day40-network

docker exec -it day40-nginx bash

ping day40-postgres

## Key Learnings

* Multi-tier architecture
* Docker DNS
* Service-to-service communication
* Container networking
* Real-world microservice patterns

## Outcome

Successfully connected two containers through a custom Docker network and verified communication using Docker DNS.

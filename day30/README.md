# Day 30 - Docker Networking

## Topics Covered
- Docker Networks
- Container Communication
- DNS Resolution in Docker

## Commands Used

Create Network:
docker network create day30-network

Run Containers:
docker run -dit --name day30-container1 --network day30-network ubuntu
docker run -dit --name day30-container2 --network day30-network ubuntu

Access Container:
docker exec -it day30-container1 bash

Install Ping:
apt update
apt install -y iputils-ping

Test Connectivity:
ping day30-container2

## Outcome
Successfully created a custom Docker network and verified communication between containers using container names.
# Day 22 - Docker Networking

## Objective
Learn how Docker networking enables communication between containers.

## What I Learned

- Docker networks
- Bridge network
- Creating custom networks
- Connecting containers to the same network
- Container-to-container communication

## Commands Used

```bash
docker network ls

docker network create mynetwork

docker run -dit --name container1 --network mynetwork ubuntu

docker run -dit --name container2 --network mynetwork ubuntu

docker network inspect mynetwork

docker exec -it container1 bash

apt update
apt install -y iputils-ping

ping container2
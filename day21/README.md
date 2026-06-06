# Day 21 - Docker Volumes

## Objective
Learn how Docker volumes provide persistent storage.

## What I Learned
- Creating Docker volumes
- Mounting volumes to containers
- Storing data outside containers
- Data persistence after container deletion

## Commands Used

```bash
docker volume create mydata
docker volume ls

docker run -dit --name volume-demo -v mydata:/data ubuntu

docker exec volume-demo bash -c "echo 'Hello Day21' > /data/test.txt"

docker stop volume-demo
docker rm volume-demo

docker run -dit --name volume-demo-new -v mydata:/data ubuntu

docker exec volume-demo-new cat /data/test.txt
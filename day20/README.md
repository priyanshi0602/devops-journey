# Day 20 - Custom Docker Image

## Objective
Build and run a custom Docker image using NGINX.

## What I Learned
- Dockerfile basics
- Building images with docker build
- Running containers with docker run
- Port mapping
- Serving custom HTML with NGINX

## Commands Used

```bash
docker build -t priyanshi-nginx .
docker run -d -p 8081:80 priyanshi-nginx
docker ps
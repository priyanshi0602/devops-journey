# Day 38 - Docker Bind Mounts

## Objective
Learn how Docker Bind Mounts connect host files directly to containers.

## Commands Used

Create Nginx container with bind mount:

```bash
docker run -d \
--name day38-nginx \
-p 8086:80 \
-v $(pwd):/usr/share/nginx/html \
nginx
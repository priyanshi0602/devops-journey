# Day 34 - Docker Hub & Image Registry

## Objective
Learn how Docker images are shared using Docker Hub.

## Commands Used

### Login

```bash
docker login
```

### Tag Image

```bash
docker tag day33-nginx priyanshi0602/day33-nginx:v1
```

### Push Image

```bash
docker push priyanshi0602/day33-nginx:v1
```

### Verify Image

```bash
docker pull priyanshi0602/day33-nginx:v1
```

## Docker Hub Repository

https://hub.docker.com/r/priyanshi0602/day33-nginx

## Learning

- Docker images can be shared globally.
- Docker Hub acts like GitHub for Docker images.
- Tagging creates versions.
- Images can be pulled on any machine.
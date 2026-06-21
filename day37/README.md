# Day 37 - Docker Volumes and Persistent Storage

## Objective

Learn how Docker volumes provide persistent storage independent of containers.

## Commands Used

```bash
docker volume create day37-data

docker volume ls

docker run -v day37-data:/app/data ubuntu

docker volume inspect day37-data
```

## What I Learned

* Docker Named Volumes
* Persistent Data Storage
* Volume Lifecycle
* Volume Inspection
* Data survives container deletion

## Outcome

Created a Docker volume, stored data inside it, deleted the original container, and verified the data still existed when a new container mounted the same volume.

## Screenshots

Stored inside screenshots folder.

```
```

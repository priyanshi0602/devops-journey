# Day 32 - Docker Volumes

## Objective

Learn how Docker Volumes provide persistent storage independent of containers.

## Commands Used

docker volume create day32-volume

docker volume ls

docker volume inspect day32-volume

docker run -it -v day32-volume:/data ubuntu bash

## Experiment

1. Created a Docker Volume.
2. Mounted it inside a container.
3. Created a file in the volume.
4. Deleted the container.
5. Started a new container using the same volume.
6. Verified the file still existed.

## Key Learning

Docker Volumes allow data to survive container deletion and are essential for databases and production applications.

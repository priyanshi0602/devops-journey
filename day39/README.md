# Day 39 - Docker Networking

## Objective

Learn Docker custom networks and container-to-container communication.

## Commands Used

### Create Network

```bash
docker network create day39-network
```

### Create Containers

```bash
docker run -dit --name container1 --network day39-network ubuntu bash

docker run -dit --name container2 --network day39-network ubuntu bash
```

### Access Container

```bash
docker exec -it container1 bash
```

### Install Ping

```bash
apt update
apt install iputils-ping -y
```

### Test Connectivity

```bash
ping container2
```

### Inspect Network

```bash
docker network inspect day39-network
```

## Key Learnings

* Docker provides built-in DNS resolution.
* Containers communicate using container names.
* Custom networks isolate workloads.
* Container-to-container communication is the foundation of microservices.
* Docker networking concepts are heavily used in Kubernetes.

## Screenshots

1. Network Creation
2. Running Containers
3. Ping Test
4. Network Inspection
5. Docker DNS Resolution

# Day 24 - Dockerizing a Flask Application

## Objective

Learn how to containerize a Python Flask application using Docker.

## Project Structure

app.py
requirements.txt
Dockerfile
README.md

## What I Learned

- Dockerizing applications
- Creating a Dockerfile for Python apps
- Building Docker images
- Running containers
- Port mapping

## Commands Used

```bash
docker build -t flask-day24 .

docker run -d -p 5000:5000 --name flask-app flask-day24

docker ps
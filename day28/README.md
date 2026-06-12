# Day 28 - Environment Variables with Docker Compose

## Objective

Learn how to use environment variables with Docker Compose and Flask applications.

## Project Structure

* app.py
* requirements.txt
* Dockerfile
* docker-compose.yml
* .env
* README.md

## What I Learned

* Environment variables
* .env files
* Configuration management
* Docker Compose environment injection
* Separating configuration from code

## Commands Used

docker compose up -d

docker compose ps

docker compose down

## Result

Successfully passed environment variables from a .env file into a Flask application.

Examples:

APP_NAME=Priyanshi DevOps App

APP_NAME=Day 28 Environment Variables Demo

The application updated automatically after restarting the containers.

## Key Takeaway

Environment variables allow applications to be configured without modifying source code.

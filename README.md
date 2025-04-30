# Kupe House API

A Flask-based API that provides information about Kupe House at Macleans College and the legendary Polynesian explorer Kupe. <https://kupe-house.qincai.xyz>

## Features

- Random fact endpoint (`/api/fact`)
- Chat endpoint with AI responses (`/api/chat`)
- Rate limiting to prevent abuse
- Request logging
- CORS support

## Tech Stack

- Python/Flask
- Groq API (using Llama 4 Scout model)
- Docker for containerization
- GitHub Actions for CI/CD

## CI/CD

This project uses GitHub Actions for continuous deployment to a self-hosted runner(my Pi). When changes are pushed to the master branch, the workflow in `.github/workflows/update-local.yml` automatically updates the Docker container on my server.

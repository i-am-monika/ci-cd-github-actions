# CI/CD Pipeline with GitHub Actions

Automated CI/CD pipeline for a Python Flask app using GitHub Actions — triggers on every push to main/master.

## Pipeline Jobs
- **Build & Test** — installs dependencies, runs pytest, builds Docker image
- **Code Quality** — flake8 linting for clean code standards
- **Security Scan** — safety check on dependencies for vulnerabilities

## Tech Stack
GitHub Actions · Python · Flask · Docker · pytest · flake8

## How it works
Every git push triggers the pipeline automatically — no manual intervention needed.

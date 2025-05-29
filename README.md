# AWS BI Dashboard Demo

This project is designed to demonstrate:

- GitHub-based version control
- Docker containerization
- Jenkins CI/CD integration
- Multi-container setup with Docker Compose
- Deployment on AWS ECS (Fargate)

## Structure

- `/bi-dashboard-app`: Streamlit-based BI app
- `/jenkins`: Jenkins pipeline file
- `/docker-compose`: Compose file for multi-container orchestration

## How to Run Locally

```bash
cd docker-compose
docker-compose up --build

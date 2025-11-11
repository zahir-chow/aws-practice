# Django REST Framework Project with PostgreSQL and Docker

This is a simple Django REST Framework project with a custom user model, PostgreSQL database, Docker support, and Jenkins CI/CD pipeline.

## Features

- Custom User model extending AbstractBaseUser
- Django REST Framework API
- PostgreSQL database integration
- Docker containerization
- Jenkins CI/CD pipeline
- Health check endpoint

## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment: `source .venv/bin/activate` (Linux/Mac) or `.venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create a superuser: `python manage.py createsuperuser`
7. Run the development server: `python manage.py runserver`

## Docker Setup

1. Build and run with Docker Compose: `docker-compose up --build`
2. Access the application at `http://localhost:8000`

## API Endpoints

- Admin: `/admin/`
- API: `/accounts/api/`
  - Users list: `/accounts/api/users/`
  - User detail: `/accounts/api/users/{id}/`
  - Health check: `/accounts/api/health/`

## Jenkins Pipeline

The Jenkinsfile defines a pipeline with the following stages:
1. Checkout
2. Setup Python Environment
3. Run Tests
4. Build Docker Image
5. Push Docker Image
6. Deploy
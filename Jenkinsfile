pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "myproject-app"
        DOCKER_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/zahir-chow/aws-practice.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    echo 'Using system Python...'
                    // Just check if Python is available
                    sh 'python --version || python3 --version || echo "Python not found"'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo 'Skipping tests for now...'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker image...'
                    // Try to build Docker image
                    sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} . || echo "Docker build failed or Docker not available"'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    echo 'Skipping Docker push...'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo 'Deployment skipped...'
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
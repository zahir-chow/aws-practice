pipeline {
    agent {
        docker {
            image 'python:3.11'
        }
    }

    environment {
        DOCKER_IMAGE = "myproject-app"
        DOCKER_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/zahir-chow/aws-practice'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python manage.py test'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // We need to install Docker CLI in the Python container
                    sh 'apt-get update && apt-get install -y docker.io'
                    sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // This would require Docker Hub credentials
                    echo 'Pushing Docker image...'
                    // Uncomment and configure when you have Docker Hub credentials
                    // sh 'docker login -u $DOCKER_USER -p $DOCKER_PASS'
                    // sh 'docker push ${DOCKER_IMAGE}:${DOCKER_TAG}'
                    // sh 'docker push ${DOCKER_IMAGE}:latest'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Add deployment steps here
                    echo 'Deploying application...'
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
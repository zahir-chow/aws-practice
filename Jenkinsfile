pipeline {
    agent any

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
                sh 'python3 -m venv venv || python -m venv venv'
                sh 'source venv/bin/activate && pip install -r requirements.txt || venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'source venv/bin/activate && python manage.py test || venv\\Scripts\\python manage.py test'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // This will only work if Docker is installed on the Jenkins host
                    sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} . || echo "Docker not available on this agent"'
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
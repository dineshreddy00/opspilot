pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out OpsPilot source code...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building OpsPilot Docker image...'
                sh 'docker build -t opspilot:latest .'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying OpsPilot container...'
                sh '''
                    docker rm -f opspilot-app || true
                    docker run -d --name opspilot-app -p 5000:5000 opspilot:latest
                '''
            }
        }
    }
}

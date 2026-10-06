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
    }
}

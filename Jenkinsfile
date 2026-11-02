pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code retrieved from GitHub'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker image'
                sh 'docker build -t ecommerce-app:latest .'
            }
        }

        stage('Test') {
            steps {
                echo 'Running application tests'
                sh 'docker run --rm ecommerce-app:latest pytest -v'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Docker image successfully built and tested'
            }
        }
    }
}
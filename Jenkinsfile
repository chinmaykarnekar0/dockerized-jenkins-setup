pipeline {

    agent any

    environment {

        PROJECT_NAME = "dockerized-jenkins-setup"

    }

    stages {

        stage('Validate Environment') {

            steps {

                echo 'Validating Jenkins environment...'

                sh 'docker --version'
                sh 'git --version'
                sh 'python --version || true'
            }
        }

        stage('Validate Docker Compose') {

            steps {

                echo 'Validating Docker Compose configuration...'

                sh 'docker compose config'
            }
        }

        stage('Build Jenkins Image') {

            steps {

                echo 'Building Jenkins Docker image...'

                sh 'docker compose build'
            }
        }

        stage('Verify Running Containers') {

            steps {

                echo 'Checking running containers...'

                sh 'docker ps'
            }
        }
    }

    post {

        always {

            echo 'Pipeline execution completed.'
        }

        success {

            echo 'Pipeline executed successfully.'
        }

        failure {

            echo 'Pipeline execution failed.'
        }
    }
}
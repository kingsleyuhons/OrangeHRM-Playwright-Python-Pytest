pipeline {
    agent any

    stages {

        stage('Check Python') {
            steps {
                bat 'python --version'
                bat 'pip --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
                bat 'playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest -v'
            }
        }
    }
}

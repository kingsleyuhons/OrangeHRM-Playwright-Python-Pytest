pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
                bat 'playwright install'
            }
        }

        stage('Run tests') {
            steps {
                bat 'pytest -v'
            }
        }
    }
}

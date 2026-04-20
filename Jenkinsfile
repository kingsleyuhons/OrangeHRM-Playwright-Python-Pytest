pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/kingsleyuhons/OrangeHRM-Playwright-Python-Pytest.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
                bat 'playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest --maxfail=1 --disable-warnings -v'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/*.html', allowEmptyArchive: true
        }
    }
}

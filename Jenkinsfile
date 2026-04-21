pipeline {
    agent any

    stages {

        stage('Setup Environment') {
            steps {
                bat '"C:\\Users\\USER\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv venv'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
                bat 'venv\\Scripts\\activate && playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\activate && pytest -v -n auto --html=report.html --self-contained-html'
            }
        }
    }
post {
        slackSend(
    tokenCredentialId: 'Slack-token',
    channel: '#all-personal-projects',
    message: 'Test message from Jenkins'
)
    }
    success {
        slackSend(
            tokenCredentialId: 'Slack-token',
            channel: '#all-personal-projects',
            color: 'good',
            message: "✅ SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}\n${env.BUILD_URL}"
        )
    }
    failure {
        slackSend(
            tokenCredentialId: 'Slack-token',
            channel: '#all-personal-projects',
            color: 'danger',
            message: "❌ FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}\n${env.BUILD_URL}"
        )
    }
}
}

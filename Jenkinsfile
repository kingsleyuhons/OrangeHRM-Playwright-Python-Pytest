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
        success {
            slackSend(
                webhookUrl: 'https://hooks.slack.com/services/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',
                color: 'good',
                message: "✅ SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}\n${env.BUILD_URL}"
            )
        }
        failure {
            slackSend(
                webhookUrl: 'YOUR_WEBHOOK_URL',
                color: 'danger',
                message: "❌ FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}\n${env.BUILD_URL}"
            )
        }
    }
}

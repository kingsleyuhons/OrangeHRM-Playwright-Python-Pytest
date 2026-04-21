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
        script {
            withCredentials([string(credentialsId: 'slack-token', variable: 'SLACK_TOKEN')]) {
                bat '''
                curl -X POST -H "Authorization: Bearer %SLACK_TOKEN%" ^
                -H "Content-type: application/json" ^
                --data "{\\"channel\\":\\"#all-personal-projects\\",\\"text\\":\\"✅ SUCCESS: %JOB_NAME% #%BUILD_NUMBER%\\n%BUILD_URL%\\"}" ^
                https://slack.com/api/chat.postMessage
                '''
            }
        }
    }

    failure {
        script {
            withCredentials([string(credentialsId: 'slack-token', variable: 'SLACK_TOKEN')]) {
                bat '''
                curl -X POST -H "Authorization: Bearer %SLACK_TOKEN%" ^
                -H "Content-type: application/json" ^
                --data "{\\"channel\\":\\"#all-personal-projects\\",\\"text\\":\\"❌ FAILED: %JOB_NAME% #%BUILD_NUMBER%\\n%BUILD_URL%\\"}" ^
                https://slack.com/api/chat.postMessage
                '''
            }
        }
    }
}
}

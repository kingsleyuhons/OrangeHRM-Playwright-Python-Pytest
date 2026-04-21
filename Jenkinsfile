pipeline {
    agent any

    stages {

        stage('Setup Environment') {
            steps {
                bat '"C:\\Users\\USER\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv venv'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
                bat 'venv\\Scripts\\activate && playwright install'
                bat """
                curl -F file=@screenshots/test_name.png ^
                -F "channels=#all-personal-projects" ^
                -H "Authorization: Bearer %SLACK_TOKEN%" ^
                https://slack.com/api/files.upload
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\activate && pytest -v -n auto --html=report.html --self-contained-html'
            }
        }
    }

post {
    always {
        script {

            // Parse test results
            def output = bat(
                script: 'venv\\Scripts\\activate && python parse_results.py',
                returnStdout: true
            ).trim()

            def total = (output =~ /TOTAL=(\d+)/)[0][1]
            def passed = (output =~ /PASSED=(\d+)/)[0][1]
            def failed = (output =~ /FAILED=(\d+)/)[0][1]

            def reportUrl = "${env.BUILD_URL}artifact/report.html"

            withCredentials([string(credentialsId: 'slack-token', variable: 'SLACK_TOKEN')]) {

                bat """
                curl -X POST -H "Authorization: Bearer %SLACK_TOKEN%" ^
                -H "Content-type: application/json" ^
                --data "{\\"channel\\":\\"#all-personal-projects\\",
                \\"text\\":\\"📊 *Test Results*\\n
                Total: ${total}\\n
                Passed: ${passed}\\n
                Failed: ${failed}\\n
                🔗 Report: ${reportUrl}\\"}" ^
                https://slack.com/api/chat.postMessage
                """
            }
        }
    }
}
    post {
    always {
        archiveArtifacts artifacts: 'report.html', fingerprint: true
    }
}
}

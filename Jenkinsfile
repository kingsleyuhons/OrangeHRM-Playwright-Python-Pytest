pipeline {
    agent any

    stages {

        stage('Setup Environment') {
            steps {
                bat '"C:\\Users\\USER\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv venv'
                bat 'venv\\Scripts\\activate && python -m pip install --upgrade pip'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
                bat 'venv\\Scripts\\activate && playwright install'
                
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                venv\\Scripts\\activate && pytest -v -n auto --html=report.html --self-contained-html --junitxml=results.xml
                """
            }
        }

        stage('Debug Files') {
            steps {
                bat 'dir'
                bat 'type results.xml'
            }
        }
    }

    post {
        always {
            script {

                // Parse results
                def output = bat(
                    script: 'venv\\Scripts\\activate && python utils\\parse_results.py',
                    returnStdout: true
                ).trim()

                echo "Parsed Output:\n${output}"

                def total = (output =~ /TOTAL=(\\d+)/)[0][1]
                def passed = (output =~ /PASSED=(\\d+)/)[0][1]
                def failed = (output =~ /FAILED=(\\d+)/)[0][1]

                def reportUrl = "${env.BUILD_URL}artifact/report.html"

                // Send Slack notification safely (NO multiline issues)
                withCredentials([string(credentialsId: 'slack-token', variable: 'SLACK_TOKEN')]) {

                    def message = """Test Results:
                    Total: ${total}
                    Passed: ${passed}
                    Failed: ${failed}
                    Report: ${reportUrl}"""

                    bat """
                    curl -X POST ^
                    -H "Authorization: Bearer %SLACK_TOKEN%" ^
                    -H "Content-type: application/json" ^
                    --data "{\\"channel\\":\\"#all-personal-projects\\",\\"text\\":\\"${message}\\"}" ^
                    https://slack.com/api/chat.postMessage
                    """
                }
            }

            // Archive report
            archiveArtifacts artifacts: 'report.html', fingerprint: true
        }
    }
}

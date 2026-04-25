pipeline {
    agent any

    stages {

        stage('Setup Environment') {
            steps {
                bat '"C:\\Users\\USER\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv venv'
                bat 'venv\\Scripts\\activate && python -m pip install --upgrade pip'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
                bat 'venv\\Scripts\\activate && playwright install'
                bat 'venv\\Scripts\\activate && pip install pytest-xdist pytest-html pytest-metadata'
                
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\activate && pytest -v -n auto pytest --junitxml=results.xml --html=report.html
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

                // Archive report first
                archiveArtifacts artifacts: 'report.html', fingerprint: true

                // Parse results
                def output = bat(
                    script: 'venv\\Scripts\\activate && python utils\\parse_results.py',
                    returnStdout: true
                ).trim()

                def total = (output =~ /TOTAL=(\d+)/)[0][1]
                def passed = (output =~ /PASSED=(\d+)/)[0][1]
                def failed = (output =~ /FAILED=(\d+)/)[0][1]

                def reportUrl = "${env.BUILD_URL}artifact/report.html"

                withCredentials([string(credentialsId: 'slack-token', variable: 'SLACK_TOKEN')]) {

                    // Send summary message
                  bat """
                    curl -X POST -H "Authorization: Bearer %SLACK_TOKEN%" ^
                    -H "Content-type: application/json" ^
                    --data "{\\"channel\\":\\"#all-personal-projects\\",\\"text\\":\\"Test Results - Total: ${total}, Passed: ${passed}, Failed: ${failed}, Report: ${reportUrl}\\"}" ^
                    https://slack.com/api/chat.postMessage
                    """

                    // Upload screenshots ONLY if failures exist
                    if (failed.toInteger() > 0) {
                        bat """
                        for %%f in (screenshots\\*.png) do (
                            curl -F file=@%%f ^
                            -F "channels=#all-personal-projects" ^
                            -H "Authorization: Bearer %SLACK_TOKEN%" ^
                            https://slack.com/api/files.upload
                        )
                        """
                    }
                }
            }
        }
    }
}

pipeline {
    agent any

    stages {

        stage('Setup Environment') {
            steps {
                bat '"C:\\Users\\USER\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv venv'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
                bat 'venv\\Scripts\\activate && playwright install'
                bat '''
                curl -X POST -H "Authorization: Bearer xoxb-10958129923474-10951760720947-Mnhys82R0DbG2mKwTuTJ6WwM" ^
                -H "Content-type: application/json" ^
                --data "{\\"channel\\":\\"#all-personal-projects\\",\\"text\\":\\"Test from Jenkins\\"}" ^
                https://slack.com/api/chat.postMessage
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\activate && pytest -v -n auto --html=report.html --self-contained-html'
            }
        }
    }


}

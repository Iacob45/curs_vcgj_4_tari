pipeline {
    agent any

    stages {
        stage('Clonare repo') {
            steps {
                git 'https://github.com/Iacob45/curs_vcgj_4_tari.git'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip install -r quickrequirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Run app') {
            steps {
                sh 'python tari.py &'
            }
        }
    }
}

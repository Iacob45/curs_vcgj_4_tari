pipeline {
    agent any

    environment {
        // Adaugăm venv în PATH astfel încât python, pip, pytest, pylint din .venv să fie disponibile
        VENV_DIR = "${WORKSPACE}/.venv"
        PATH = "${WORKSPACE}/.venv/bin:${env.PATH}"
    }

    stages {
        stage('Setup Python venv') {
            steps {
                echo 'Creating and activating virtualenv…'
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image tari:v${BUILD_NUMBER}…"
                sh 'docker build -t tari:v${BUILD_NUMBER} .'
            }
        }

        stage('Code Quality (pylint)') {
            steps {
                echo 'Running pylint…'
                sh '''
                    . .venv/bin/activate
                    export PYTHONPATH=.
                    pylint --exit-zero $(find app/lib -name "*.py")
                    pylint --exit-zero $(find app/tests -name "*.py")
                    pylint --exit-zero tari.py
                '''
            }
        }

        stage('Unit Tests (pytest)') {
            steps {
                echo 'Running pytest…'
                sh '''
                    . .venv/bin/activate
                    pytest -q app/tests/
                '''
            }
        }

        stage('Run Container') {
            steps {
                echo "Starting container tari${BUILD_NUMBER} on host port 8020…"
                sh '''
                    docker run -d --name tari${BUILD_NUMBER} -p 8020:5011 tari:v${BUILD_NUMBER}
                '''
            }
        }
    }

    post {
        always {
            echo 'Cleaning up Docker container…'
            sh '''
                docker stop tari${BUILD_NUMBER} || true
                docker rm tari${BUILD_NUMBER} || true
            '''
        }
    }
}


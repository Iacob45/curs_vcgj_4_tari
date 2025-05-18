pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo ' Building...'
                sh '''
                    pwd
                    ls -l
                    ./activeaza_venv_jenkins
                '''
            }
        }

        stage('Pylint - Calitate Cod') {
            steps {
                sh '''
                    ./activeaza_venv_jenkins;
                    pylint --exit-zero app/lib/*.py
                    pylint --exit-zero app/test/*.py
                    pylint --exit-zero tari.py
                '''
            }
        }

        stage('Unit Testing cu Pytest') {
            steps {
                echo ' Unit testing with pytest...'
                sh '''
                    ./activeaza_venv_jenkins;
                    pytest
                '''
            }
        }

        stage('Docker Build') {
            steps {
                echo " Creare imagine docker"
                sh '''
                    docker build -t tari:v${BUILD_NUMBER} .
                '''
            }
        }

        stage('Running Container') {
            steps {
                echo "Pornește containerul..."
                sh '''
                    docker run -d --name tari${BUILD_NUMBER} -p 8020:5011 tari:v${BUILD_NUMBER}
                '''
            }
        }
    }
}               



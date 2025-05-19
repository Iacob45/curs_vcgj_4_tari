pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh '''
                    pwd
                    ls -l
                    . ./activeaza_venv_jenkins
                '''
            }
        }

        stage('Pylint - Calitate Cod') {
             agent any
             steps {
                sh '''
                   chmod +x ./activeaza_venv_jenkins;
                   . ./activeaza_venv;
                   export PYTHONPATH=.;
                   pylint --exit-zero app/lib/biblioteca_grecia.py;
	           pylint --exit-zero app/test/test_biblioteca_grecia.py;
                   pylint --exit-zero tari.py
        '''
    }
}

        stage('Unit Testing cu pytest') {
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    . ./activeaza_venv
                    flask --app tari test
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo "Build ID: ${BUILD_NUMBER}"
                echo "Creare imagine docker"
                sh '''
                    docker build -t tari:v${BUILD_NUMBER} .
                '''
                // docker create --name tari${BUILD_NUMBER} -p 8020:5011 tari:v${BUILD_NUMBER}
            }
        }

        stage('Running') {
            steps {
                echo "Pornesc containerul"
                sh '''
                    docker run -d --name tari${BUILD_NUMBER} -p 8020:5011 tari:v${BUILD_NUMBER}
                '''
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh '''
                docker ps -a | grep tari | grep -v ${BUILD_NUMBER} | awk '{print $1}' | xargs -r docker stop
                docker ps -a | grep tari | grep -v ${BUILD_NUMBER} | awk '{print $1}' | xargs -r docker rm
            '''
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}

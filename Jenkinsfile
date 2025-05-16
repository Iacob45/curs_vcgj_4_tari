/*Jenkins*/
pipeline {
    agent any

    stages {
        stage('Build') {
            agent any
            steps {
                echo 'Building...'
                sh '''
                    pwd;
                    ls -l;
                    . ./activeaza_venv_jenkins
                    '''
            }
        }
        

        stage('Controlul calitatii cu pylint') {
            agent any
            steps {
                sh '''
                    . ./activeaza_venv;
					export PYTHONPATH=.
					
                    echo '\n\nVerificare lib/*.py cu pylint\n';
                    pylint --exit-zero app/lib/biblioteca_honduras;

                    echo '\n\nVerificare test_biblioteca_honduras.py cu pylint\n';
                    pylint --exit-zero app/tests/test_biblioteca_honduras.py;

                    echo '\n\nVerificare tari.py cu pylint\n';
                    pylint --exit-zero tari.py;
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            agent any
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    . ./activeaza_venv;
					export PYTHONPATH=.
                    pytest;
                    
                '''
            }
        }
        
        stage('Deploy') {
            agent any
            steps {
                echo "Build ID: ${BUILD_NUMBER}"
                echo "Creare imagine docker"
                sh '''
                    docker build -t tari:v${BUILD_NUMBER} .
                '''
            }
			
        }
		stage('Running') {
            agent any
            steps {
                echo "Pornesc containerul"
                sh '''
                    docker run -d --name tari${BUILD_NUMBER} -p 8020:5011 tari:v${BUILD_NUMBER}
                '''
            }
			
        }
    }
}

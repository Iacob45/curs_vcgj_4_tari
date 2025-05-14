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
        

        stage('pylint - calitate cod') {
            agent any
            steps {
                sh '''
                    . ./activeaza_venv;
					export PYTHONPATH=.
					
                    echo '\n\nVerificare lib/*.py cu pylint\n';
                    pylint --exit-zero $(find app/lib -name "*.py");

                    echo '\n\nVerificare tests/*.py cu pylint';
                    pylint --exit-zero $(find app/tests -name "*.py");

                    echo '\n\nVerificare tari.py cu pylint';
                    pylint --exit-zero tari.py;
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            agent anys
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    . ./activeaza_venv;
                    pytest app/tests/
                    
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
				/*docker create --name tari${BUILD_NUMBER} -p 8020:5011 tari:v${BUILD_NUMBER}*/
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

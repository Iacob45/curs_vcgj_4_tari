pipeline {
    agent any

    environment {
        // Setează variabila de mediu pentru Flask
        FLASK_APP = 'tari.py'
    }

    stages {
        // Pasul 1: Build
        stage('Build') {
            steps {
                echo 'Building the application...'
                sh '''
                    pwd
                    ls -l
                    
                    # Crearea mediului virtual (doar o dată)
                    python3 -m venv .venv
                    
                    # Activează mediul virtual
                    . ./.venv/bin/activate

                    # Instalarea dependențelor
                    pip install -r requirements.txt
                '''
            }
        }

        // Pasul 2: Verificare calitate cod cu pylint
        stage('pylint - Calitate Cod') {
            steps {
                echo 'Running pylint on Python files...'
                sh '''
                    . ./.venv/bin/activate  # Activează mediul virtual
                    pylint --exit-zero lib/*.py
                    pylint --exit-zero tests/*.py
                    pylint --exit-zero tari.py
                '''
            }
        }

        // Pasul 3: Testare unitară cu pytest
        stage('Unit Testing cu pytest') {
            steps {
                echo 'Running unit tests with Pytest...'
                sh '''
                    . ./.venv/bin/activate  # Activează mediul virtual
                    pytest --maxfail=1 --disable-warnings -q  # Execută testele cu pytest
                '''
            }
        }

        // Pasul 4: Crearea imaginii Docker
        stage('Creare Imagine Docker') {
            steps {
                echo "Creating Docker image"
                sh '''
                    docker build -t tari:v${BUILD_NUMBER} .
                '''
            }
        }

        // Pasul 5: Rularea containerului Docker
        stage('Running Docker Container') {
            steps {
                echo "Running the Docker container"
                sh '''
                    docker run -d --name tari${BUILD_NUMBER} -p 8020:5011 tari:v${BUILD_NUMBER}
                '''
            }
        }

        // Pasul 6: Testarea aplicației din container
        stage('Testare Aplicație Docker') {
            steps {
                echo 'Testarea aplicației cu Olanda...'
                sh '''
                    curl http://localhost:8020/olanda  # Verifică că aplicația funcționează la adresa respectivă
                '''
            }
        }

        // Pasul 7: Curățare (opțional)
        stage('Cleanup') {
            steps {
                echo 'Removing Docker container'
                sh '''
                    docker rm -f tari${BUILD_NUMBER}
                    docker rmi tari:v${BUILD_NUMBER}
                '''
            }
        }
    }

    post {
        always {
            echo 'This will always run at the end of the pipeline.'
        }
        success {
            echo 'The pipeline ran successfully.'
        }
        failure {
            echo 'The pipeline failed. Check the logs above for details.'
        }
    }
}


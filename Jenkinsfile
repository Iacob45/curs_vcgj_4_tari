pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Install') {
      steps { sh '''
      python3 -m venv venv
          . venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
'''}
    }
    stage('Test') {    
      steps {sh '''
      . venv/bin/activate
      python3 -m pip install -r requirements.txt
export PYTHONPATH=$(pwd)      
      pytest --maxfail=1 --disable-warnings -q
    '''}
    }
    stage('Build Docker image'){
       steps {
sh 'docker build -t egipt_app .'
	}
    }
  }
  post {
    always {
     echo 'pipeline-ul e gata' 
    }
  }
}

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
	stage('Run Docker')
{
steps
{
sh '''
if docker ps -a --format '{{.Names}}' | grep -q '^egipt_containers$'; then
docker stop egipt_container || true
docker rm egipt_container || true
fi
docker run -d --name egipt_container -p 5011:5000 egipt_app
'''
}

}




  }
  post {
    always {
     echo 'pipeline-ul e gata' 
    }
  }
}

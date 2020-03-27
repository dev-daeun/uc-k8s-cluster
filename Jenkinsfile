pipeline {
    agent {
        docker {
            image 'kde6260/jenkins-agent:latest'
            args '-u root:root'
        }
    }
    environment {
        FLASK_APP = 'app/app:flask_app'
    }
    stages {
        stage('Lint Python code') {
            steps {
                sh 'pip install --upgrade pip'
                sh 'pip install flake8==3.7.9'
                sh 'python3 -m flake8 app/app.py --ignore=E501'
            }
        }
        stage('Lint Dockerfile') {
            steps {
                sh 'hadolint docker/app/Dockerfile --ignore DL3013'
                sh 'hadolint docker/app/Dockerfile --ignore DL3013'
            }
        }
        stage('Test API') {
            steps {
                sh 'pip install -r app/requirements.txt'
                sh 'flask run --port 5000'
                sh 'pytest tests.py'
                sh "pgrep -f 'flask run --port 5000' | xargs kill"
            }
        }
    }
}


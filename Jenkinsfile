pipeline {
    agent {
        docker {
            image 'kde6260/jenkins-agent'
        }
    }
    environment {
        FLASK_APP = 'app/app:flask_app'
    }
    stages {
        stage('Lint Python code') {
            steps {
                sh 'cd /home/testuser'
                sh 'pyenv activate test-environ'
                sh 'pip install --upgrade pip'
                sh 'pip install flake8==3.7.9'
                sh 'python -m flake8 app/app.py --ignore=E501'
            }
        }
        stage('Lint Dockerfile') {
            steps {
                sh 'wget -O ./hadolint https://github.com/hadolint/hadolint/releases/download/v1.16.3/hadolint-Linux-x86_64'
                sh 'chmod +x ./hadolint'
                sh './hadolint docker/app/Dockerfile --ignore DL3013'
                sh './hadolint docker/app/Dockerfile --ignore DL3013'
            }
        }
        stage('Test API') {
            steps {
                sh 'pip install -r app/requirements.txt'
                sh 'flask run --port 5000 &'
                sh 'pytest app/tests.py'
                sh "pgrep -f 'flask run --port 5000' | xargs kill"
            }
        }
    }
}


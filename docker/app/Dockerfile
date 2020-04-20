FROM python:3.7.3-stretch

RUN mkdir /home/uc-k8c-cluster

WORKDIR /home/uc-k8c-cluster

COPY . /home/uc-k8c-cluster

RUN pip install --upgrade pip && pip install --trusted-host pypi.python.org -r app/requirements.txt

EXPOSE 9090

WORKDIR /home/uc-k8c-cluster/app

ENTRYPOINT ['gunicorn',  '--workers=2', '--bind 0.0.0.0:9090', 'app:flask_app']

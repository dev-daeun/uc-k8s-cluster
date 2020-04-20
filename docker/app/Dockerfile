FROM python:3.7-alpine

RUN mkdir -p /home/uc-k8s-cluster/app
COPY ./app /home/uc-k8s-cluster/app
WORKDIR /home/uc-k8s-cluster/app

RUN pip install --upgrade pip && pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 9090

ENTRYPOINT gunicorn --workers=2 --bind 0.0.0.0:9090 app:flask_app

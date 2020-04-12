FROM python:3.7.3-stretch

RUN mkdir /home/udacity-capstone

WORKDIR /home/udacity-capstone

COPY . /home/udacity-capstone

RUN pip install --upgrade pip && pip install --trusted-host pypi.python.org -r app/requirements.txt

EXPOSE 9090

ENTRYPOINT ["uwsgi", "uwsgi2.ini"]

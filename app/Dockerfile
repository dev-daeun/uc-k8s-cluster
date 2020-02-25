FROM python:3.7.3-stretch

RUN mkdir /home/udacity-capstone
WORKDIR /home/udacity-capstone

COPY . /home/udacity-capstone

RUN pwd
RUN pip install --upgrade pip && pip install wheel==0.33.6 && pip install --trusted-host pypi.python.org -r app/requirements.txt

EXPOSE 5000

ENTRYPOINT ["flask", "run"]

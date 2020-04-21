FROM python:3.7.3-stretch

# Install hadolint for linting Dockerfile
RUN wget -O /bin/hadolint https://github.com/hadolint/hadolint/releases/download/v1.16.3/hadolint-Linux-x86_64 --no-check-certificate
RUN chmod +x /bin/hadolint

# Install pip packages for linting python codes and executing unit tests.
COPY ./requirements_test.txt /home/requirements_test.txt
WORKDIR /home/
RUN pip install --upgrade pip && pip install -r requirements_test.txt

CMD /bin/bash

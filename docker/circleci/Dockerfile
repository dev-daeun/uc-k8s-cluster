FROM python:3.7.3-stretch

# Install hadolint for linting Dockerfile
RUN wget -O /bin/hadolint https://github.com/hadolint/hadolint/releases/download/v1.16.3/hadolint-Linux-x86_64 --no-check-certificate
RUN chmod +x /bin/hadolint

# Install pylint for linting Python code
RUN pip install pylint==2.4.4

CMD /bin/bash

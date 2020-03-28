FROM python:3.7.3-stretch

# User for executing pipeline steps
RUN useradd -ms /bin/bash testuser
USER testuser
WORKDIR /home/testuser

# Install hadolint for linting Dockerfile
RUN wget -O ./hadolint https://github.com/hadolint/hadolint/releases/download/v1.16.3/hadolint-Linux-x86_64
RUN chmod +x ./hadolint

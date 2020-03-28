FROM ubuntu:18.04

# Prerequisites for pyev
ENV DEBIAN_FRONTEND noninteractive
ENV TZ Asia/Seoul
RUN apt-get update -y
RUN apt-get install -y apt-utils
RUN apt-get install -y --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev \
libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev \
ca-certificates git

# User for executing pipeline steps
RUN useradd -ms /bin/bash testuser
USER testuser
WORKDIR /home/testuser

# Install hadolint for linting Dockerfile
RUN wget -O ./hadolint https://github.com/hadolint/hadolint/releases/download/v1.16.3/hadolint-Linux-x86_64 --no-check-certificate
RUN chmod +x ./hadolint

# Install pyenv
RUN git clone https://github.com/pyenv/pyenv.git ~/.pyenv
ENV HOME /home/testuser
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $HOME/.pyenv/bin:$PATH
ENV PYENV_VIRTUALENV_DISABLE_PROMPT 1
RUN pyenv install 3.7.2
RUN git clone https://github.com/pyenv/pyenv-virtualenv.git $PYENV_ROOT/plugins/pyenv-virtualenv

# Create virtualenv
COPY docker/jenkins/.bashrc ./bashrc
RUN mv ./bashrc ./.bashrc
RUN pyenv virtualenv 3.7.2 test-environ

CMD /bin/bash

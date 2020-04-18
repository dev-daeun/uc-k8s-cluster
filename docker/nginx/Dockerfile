FROM nginx:1.17.10-alpine

WORKDIR /home/udacity-capstone

COPY . /home/udacity-capstone

RUN rm /etc/nginx/nginx.conf

RUN cp ./nginx/nginx.conf /etc/nginx/nginx.conf

FROM nginx:1.16.1

WORKDIR /home/uc-k8s-cluster

COPY . /home/uc-k8s-cluster

RUN rm /etc/nginx/nginx.conf

RUN cp ./nginx/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

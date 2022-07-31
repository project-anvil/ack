# FROM registry.gitlab.com/stageright/butai:1.5.0

FROM alpine:3.5

RUN apk update && apk upgrade && apk add \
    curl \
    openssh-client \
    python \
    py-boto \
    py-dateutil \
    py-httplib2 \
    py-jinja2 \
    py-paramiko \
    py-pip \
    py-setuptools \
    py-yaml \
    shadow \
    tar && \
  pip install --upgrade pip python-keyczar && \
  rm -rf /var/cache/apk/*

RUN pip install gunicorn

RUN mkdir -p /app
COPY src /app
RUN pip install -r /app/requirements.txt
WORKDIR /app

EXPOSE 80
ENTRYPOINT []
CMD ["/usr/bin/gunicorn","-b=0.0.0.0:80","app:app"]

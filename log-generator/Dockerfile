FROM python:alpine

VOLUME [ "/var/log-generator/" ]

RUN pip install log-generator

ENTRYPOINT [ "log-generator", "/var/log-generator/log-generator.yml" ]
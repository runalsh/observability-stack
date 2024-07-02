FROM python:3.12-alpine

VOLUME [ "/etc/log-generator/" ]

RUN pip install log-generator

ENTRYPOINT [ "log-generator", "/etc/log-generator/log-generator.yml" ]
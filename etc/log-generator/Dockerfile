FROM python:3.7-alpine
# python should be 3.7

VOLUME [ "/etc/log-generator/" ]

RUN pip install log-generator

ENTRYPOINT [ "log-generator", "/etc/log-generator/log-generator.yml" ]

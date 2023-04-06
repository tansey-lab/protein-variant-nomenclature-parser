# syntax=docker/dockerfile:1.2
FROM python:3.11

RUN apt-get update -y && apt-get install -y openjdk-11-jdk

RUN --mount=type=cache,target=/.cache/pip pip install --upgrade pip && pip install twine requests

COPY . /app

RUN --mount=type=cache,target=/.cache/pip cd /app && make install

RUN cd /app && make test

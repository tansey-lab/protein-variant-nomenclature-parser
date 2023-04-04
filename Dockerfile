# syntax=docker/dockerfile:1.2
FROM python:3.11

RUN apt-get update -y && apt-get install -y build-essential antlr4

RUN pip install twine

RUN --mount=source=.git,target=.git,type=bind --mount=type=cache,target=/.cache/pip pip install --upgrade pip && pip install twine

COPY . /app

RUN --mount=source=.git,target=.git,type=bind --mount=type=cache,target=/.cache/pip cd /app && make install

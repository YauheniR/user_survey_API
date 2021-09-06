FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . /app/

RUN apt-get update && \
    pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --dev --system \

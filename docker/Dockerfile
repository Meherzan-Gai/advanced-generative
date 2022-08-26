FROM python:3.8-buster

RUN apt-get update && apt-get install -y \
    nano

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt



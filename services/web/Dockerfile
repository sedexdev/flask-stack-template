# base image
FROM python:3.11.3-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt update && apt install netcat -y

# copy over project files
COPY . .

# install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Entrypoint script
ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]

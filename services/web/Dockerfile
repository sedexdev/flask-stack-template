# base image
FROM python:3.11.3-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt update \
    && apt install curl netcat -y \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash \
    && apt install nodejs -y

# copy over project files
COPY . .

# install dependencies and audit for vulnerabilities
RUN pip install --upgrade pip && pip install -r requirements.txt && pip install pip-audit
RUN pip-audit

# check node and npm are installed
RUN node -v && npm -v

# initialiase package.json and Tailwind CSS
RUN npm init -y \
    && npm install autoprefixer postcss tailwindcss --save-dev \
    && npx tailwindcss -i ./project/static/css/input.css -o ./project/static/css/output.css --minify

# Entrypoint script
ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]

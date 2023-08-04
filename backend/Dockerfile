# Используем официальный образ Python в качестве базового образа
FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /usr/src/app

RUN apt-get update \
    && apt-get install netcat-traditional -y
RUN apt-get upgrade -y && apt-get install postgresql gcc python3-dev musl-dev -y
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy only requirements, to cache them in docker layer
COPY ./pyproject.toml ./poetry.lock* /usr/src/app/

# Project initialization:
RUN poetry install

# Creating folders, and files for a project:
COPY . /usr/src/app/
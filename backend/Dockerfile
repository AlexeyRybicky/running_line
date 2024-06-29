FROM python:3.10

ENV POETRY_VIRTUALENVS_CREATE false
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN apt-get update && apt-get install -y libgl1-mesa-glx
RUN pip install poetry
RUN poetry lock
RUN poetry install

FROM python:3.11.1

ENV PYTHONUNBUFFERED 1
ENV DONOTWRITEBYTECODE 1

WORKDIR /code

COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

COPY . /code/


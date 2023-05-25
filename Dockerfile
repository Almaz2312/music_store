FROM python:3.10-slim-bullseye
ENV PYTHONBUFFERED=1

WORKDIR /music_store

COPY . .

RUN pip install --upgrade pip \
&& pip install poetry \
&& poetry config virtualenvs.create false \
&& poetry install --no-root

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim AS builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN apt-get update -y && apt-get install libpq-dev build-essential python3-dev -y
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
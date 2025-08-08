FROM python:3.11.11-slim-bullseye

RUN pip install --upgrade pip
WORKDIR /app
COPY pyproject.toml ./
COPY . .
RUN pip install --no-cache-dir .

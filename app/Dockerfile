FROM python:3.11-slim

WORKDIR /app

COPY requirements/prod.txt .
RUN pip install -r prod.txt

COPY . .

EXPOSE 8000
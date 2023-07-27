# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.10-slim AS builder

WORKDIR /app

COPY requirements.txt /app
RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT ["python3"]
CMD ["app.py"]

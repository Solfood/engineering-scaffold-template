FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /workspace

COPY . /workspace

EXPOSE <DEFAULT_PORT>

CMD ["python3", "app/main.py"]

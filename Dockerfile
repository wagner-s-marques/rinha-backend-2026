FROM python:3.13-slim
WORKDIR /app

RUN pip install --no-cache-dir litestar granian

COPY src ./src
ENV PYTHONPATH=/app/src

EXPOSE 3000
CMD ["granian", "--interface", "asgi", "--host", "0.0.0.0", "--port", "3000", "rinha_backend_2026.app:app"]

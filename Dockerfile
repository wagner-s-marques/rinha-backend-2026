FROM python:3.13-slim
WORKDIR /app

RUN pip install --no-cache-dir litestar granian

COPY app.py fraud_score.py models.py ./
COPY resources ./resources

EXPOSE 3000
CMD ["granian", "--interface", "asgi", "--host", "0.0.0.0", "--port", "3000", "app:app"]

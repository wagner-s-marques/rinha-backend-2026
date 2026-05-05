# rinha-backend-2026
My version of Rinha Backend 2026

## Running

```bash
pip install litestar granian
granian --interface asgi --host 0.0.0.0 --port 3000 app:app
```

The server starts on port 3000.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | /status | Returns 204 if the service is up |

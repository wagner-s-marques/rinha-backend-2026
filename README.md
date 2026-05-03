# rinha-backend-2026
My version of Rinha Backend 2026

## Running

```bash
lein run
```

The server starts on port 3000.

## Building

```bash
lein uberjar
java -jar target/app.jar
```

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | /status | Returns 204 if the service is up |

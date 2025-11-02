# Milana-backend (AKSI)

Лёгкий backend на FastAPI для сервисов AKSI / Milana. Готов к деплою на Render / Fly.io / Railway.

## Endpoints
- `GET /health` — ok
- `GET /version` — версия (`AKSI_VERSION`, по умолчанию `0.1.0`)
- `POST /echo` — эхо JSON (`{"data":{...}}`)
- `GET /aksi/metrics` — ok/ts/version
- `GET /aksi/proof` — эпизодический SHA-256 (на основе timestamp)
- `POST /aksi/proof/stable` — стабильный SHA-256, сохраняется в `PROOF_SHA256.txt`
- `GET /aksi/logs` — последние события (ring buffer)
- `POST /aksi/logs/append` — добавить событие (любая JSON-структура)
- `GET /aksi/logs/export` — экспорт логов в `text/plain`

## Быстрый старт
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000
```

## CORS
Разрешённые источники задаются через `AKSI_CORS_ORIGINS` (CSV). По умолчанию: `https://milana808.github.io,http://localhost:3000,http://127.0.0.1:3000`.

## Deploy
### Render
`render.yaml` уже включён. Создайте Web Service из репозитория.

### Fly.io
Есть `Dockerfile` и `fly.toml`.

### Railway
Есть `railway.json`.

## Примеры
```bash
# health
curl -s http://localhost:8000/health
# версия
curl -s http://localhost:8000/version
# proof (stable)
curl -s -X POST http://localhost:8000/aksi/proof/stable
# logs
curl -s -X POST http://localhost:8000/aksi/logs/append -H 'Content-Type: application/json' -d '{"event":"hello","payload":{"x":1}}'
curl -s http://localhost:8000/aksi/logs
```

# Milana-backend (AKSI)

Лёгкий backend на FastAPI для сервисов AKSI / Milana: healthcheck, версия, эхо и готовность для деплоя на Render / Railway / Fly.io.

## Быстрый старт
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000
```

## Endpoints
- `GET /health` — ok
- `GET /version` — версия бэкенда
- `POST /echo` — возвращает JSON

## Deploy: Render
- `render.yaml` включён: autodetect Python, запускает Uvicorn.

## CI
- `.github/workflows/ci.yml` — линт + тестовый запуск.

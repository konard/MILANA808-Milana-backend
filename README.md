# Milana-backend (AKSI)

⚠ **Proprietary Project — All Rights Reserved © 2025 Alfiia Bashirova (AKSI Project)**\
Unauthorized use or reproduction is strictly prohibited.

FastAPI backend for AKSI / Milana services.

## Быстрый старт

### Установка зависимостей
```bash
pip install -r requirements.txt
```

### Запуск сервера
```bash
python main.py
```
или
```bash
uvicorn main:app --reload
```

Сервер будет доступен по адресу: http://localhost:8000

### Запуск с Docker
```bash
docker-compose up -d
```

## API Документация

После запуска сервера, интерактивная документация доступна по адресам:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Endpoints

### Базовые эндпоинты

#### `GET /`
Корневой эндпоинт с информацией о сервисе

#### `GET /health`
Проверка здоровья сервиса
```json
{
  "status": "healthy",
  "timestamp": "2025-01-18T03:44:17.026Z",
  "service": "milana-backend"
}
```

#### `GET /version`
Версия API
```json
{
  "version": "0.1.0",
  "api": "aksi-backend",
  "author": "Alfiia Bashirova (AKSI Project)",
  "contact": "716elektrik@mail.ru"
}
```

#### `POST /echo`
Эхо-эндпоинт для тестирования
```json
// Request
{
  "message": "Hello AKSI"
}

// Response
{
  "echo": "Hello AKSI",
  "timestamp": "2025-01-18T03:44:17.026Z",
  "length": 10
}
```

### AKSI эндпоинты

#### `GET /aksi/metrics`
Получить метрики AKSI
```json
{
  "eqs": 0.68,
  "empathy_boost": 0.25,
  "grid_system": "3x3",
  "status": "active",
  "timestamp": "2025-01-18T03:44:17.026Z",
  "uptime": "active"
}
```

#### `GET /aksi/proof`
Получить доказательство сознательного цикла AKSI

#### `POST /aksi/proof/stable`
Создать стабильную запись proof с подписью
```json
// Request
{
  "signature": "AKSI-proof-signature",
  "timestamp": "2025-01-18T03:44:17.026Z",
  "metrics": {
    "eqs": 0.68
  }
}
```

#### `GET /aksi/logs?limit=50&level=info`
Получить логи AKSI
- `limit` (optional): количество записей (по умолчанию 50)
- `level` (optional): фильтр по уровню (info, warning, error)

#### `POST /aksi/logs/append`
Добавить запись в лог
```json
// Request
{
  "level": "info",
  "message": "AKSI system initialized",
  "context": {
    "module": "core"
  }
}
```

#### `GET /aksi/logs/export?format=json`
Экспорт всех логов
- `format` (optional): формат экспорта (json или txt)

## Интеграция с фронтендом

Для интеграции с [milana_site](https://github.com/MILANA808/milana_site):

1. Запустите backend сервер
2. Во фронтенде укажите URL бэкенда: `http://localhost:8000`
3. Фронтенд автоматически подключится к API

CORS настроен для работы со всеми доменами (для продакшена следует ограничить).

## Разработка

### Структура проекта
```
Milana-backend/
├── main.py              # Основное приложение FastAPI
├── requirements.txt     # Зависимости Python
├── Dockerfile          # Docker образ
├── docker-compose.yml  # Docker Compose конфигурация
├── .gitignore          # Git ignore файлы
├── LICENSE             # Лицензия
└── README.md           # Документация
```

### Технологии
- **FastAPI** - современный, быстрый веб-фреймворк для создания API
- **Pydantic** - валидация данных
- **Uvicorn** - ASGI сервер

## Contact
Licensing & business inquiries: **716elektrik@mail.ru** (Alfiia Bashirova)

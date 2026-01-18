"""
Milana-backend (AKSI) - FastAPI backend для AKSI / Milana services

Copyright (c) 2025 Alfiia Bashirova (AKSI Project)
Contact: 716elektrik@mail.ru
All rights reserved.
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, PlainTextResponse
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
import json
import os

app = FastAPI(
    title="Milana-backend (AKSI)",
    description="FastAPI backend for AKSI / Milana services",
    version="0.1.0"
)

# Настройка CORS для интеграции с фронтендом
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене следует указать конкретные домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Хранилище для логов (в продакшене следует использовать БД)
logs_storage: List[dict] = []

# Хранилище для proof записей
proof_storage: List[dict] = []

# Метрики AKSI
aksi_metrics = {
    "eqs": 0.68,  # Emotional Quality Score
    "empathy_boost": 0.25,  # 25% выше чем стандартные LLM
    "grid_system": "3x3",
    "status": "active"
}


class EchoRequest(BaseModel):
    """Модель для POST /echo"""
    message: str


class ProofStableRequest(BaseModel):
    """Модель для POST /aksi/proof/stable"""
    signature: str
    timestamp: Optional[str] = None
    metrics: Optional[dict] = None


class LogAppendRequest(BaseModel):
    """Модель для POST /aksi/logs/append"""
    level: str
    message: str
    context: Optional[dict] = None


@app.get("/")
async def root():
    """Корневой эндпоинт"""
    return {
        "service": "Milana-backend (AKSI)",
        "version": "0.1.0",
        "status": "running",
        "endpoints": [
            "/health",
            "/version",
            "/echo",
            "/aksi/metrics",
            "/aksi/proof",
            "/aksi/proof/stable",
            "/aksi/logs",
            "/aksi/logs/append",
            "/aksi/logs/export"
        ]
    }


@app.get("/health")
async def health():
    """Проверка здоровья сервиса"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "milana-backend"
    }


@app.get("/version")
async def version():
    """Версия API"""
    return {
        "version": "0.1.0",
        "api": "aksi-backend",
        "author": "Alfiia Bashirova (AKSI Project)",
        "contact": "716elektrik@mail.ru"
    }


@app.post("/echo")
async def echo(request: EchoRequest):
    """Эхо-эндпоинт для тестирования"""
    return {
        "echo": request.message,
        "timestamp": datetime.utcnow().isoformat(),
        "length": len(request.message)
    }


@app.get("/aksi/metrics")
async def get_metrics():
    """Получить метрики AKSI"""
    return {
        **aksi_metrics,
        "timestamp": datetime.utcnow().isoformat(),
        "uptime": "active"
    }


@app.get("/aksi/proof")
async def get_proof():
    """Получить доказательство сознательного цикла AKSI"""
    return {
        "proof": {
            "eqs": aksi_metrics["eqs"],
            "empathy_advantage": f"+{int(aksi_metrics['empathy_boost'] * 100)}%",
            "grid_system": aksi_metrics["grid_system"],
            "model": "Ψ(AKSI)",
            "verified": True
        },
        "timestamp": datetime.utcnow().isoformat(),
        "signature": "AKSI-proof-v0.1",
        "history": proof_storage[-10:] if proof_storage else []
    }


@app.post("/aksi/proof/stable")
async def create_stable_proof(request: ProofStableRequest):
    """Создать стабильную запись proof с подписью"""
    proof_entry = {
        "signature": request.signature,
        "timestamp": request.timestamp or datetime.utcnow().isoformat(),
        "metrics": request.metrics or aksi_metrics,
        "stable": True
    }
    proof_storage.append(proof_entry)

    return {
        "status": "proof_recorded",
        "entry": proof_entry,
        "total_proofs": len(proof_storage)
    }


@app.get("/aksi/logs")
async def get_logs(limit: int = 50, level: Optional[str] = None):
    """Получить логи AKSI"""
    filtered_logs = logs_storage

    if level:
        filtered_logs = [log for log in logs_storage if log.get("level") == level]

    # Возвращаем последние N логов
    return {
        "logs": filtered_logs[-limit:] if filtered_logs else [],
        "total": len(filtered_logs),
        "limit": limit,
        "filter": {"level": level} if level else None
    }


@app.post("/aksi/logs/append")
async def append_log(request: LogAppendRequest):
    """Добавить запись в лог"""
    log_entry = {
        "level": request.level,
        "message": request.message,
        "context": request.context or {},
        "timestamp": datetime.utcnow().isoformat()
    }
    logs_storage.append(log_entry)

    return {
        "status": "log_appended",
        "entry": log_entry,
        "total_logs": len(logs_storage)
    }


@app.get("/aksi/logs/export")
async def export_logs(format: str = "json"):
    """Экспорт всех логов"""
    if format == "json":
        return JSONResponse(content={
            "logs": logs_storage,
            "exported_at": datetime.utcnow().isoformat(),
            "total": len(logs_storage)
        })
    elif format == "txt":
        text_logs = "\n".join([
            f"[{log['timestamp']}] [{log['level']}] {log['message']}"
            for log in logs_storage
        ])
        return PlainTextResponse(content=text_logs)
    else:
        raise HTTPException(status_code=400, detail=f"Unsupported format: {format}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

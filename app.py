from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from collections import deque
import os, hashlib, time, pathlib, json

app = FastAPI(title="Milana Backend (AKSI)")

# --- CORS ---
ALLOWED_ORIGINS = os.getenv("AKSI_CORS_ORIGINS", "https://milana808.github.io,http://localhost:3000,http://127.0.0.1:3000").split(',')
app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in ALLOWED_ORIGINS if o.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- In-memory logs (ring buffer) ---
LOG_CAP = int(os.getenv("AKSI_LOG_CAP", "200"))
_logs = deque(maxlen=LOG_CAP)

def _log(event: str, payload: dict | None = None):
    _logs.append({
        "ts": int(time.time()),
        "event": event,
        "payload": payload or {}
    })

class Echo(BaseModel):
    data: dict

@app.get("/health")
def health():
    _log("health")
    return {"status": "ok"}

@app.get("/version")
def version():
    ver = os.getenv("AKSI_VERSION", "0.1.0")
    _log("version", {"version": ver})
    return {"version": ver}

@app.post("/echo")
def echo(payload: Echo):
    _log("echo", payload.model_dump())
    return payload.model_dump()

@app.get("/aksi/metrics")
def metrics():
    ver = os.getenv("AKSI_VERSION", "0.1.0")
    data = {"ok": True, "ts": int(time.time()), "version": ver}
    _log("metrics", data)
    return data

# --- Proof: stable-on-disk within container (regenerates on new deploy) ---
PROOF_PATH = pathlib.Path("PROOF_SHA256.txt")

@app.get("/aksi/proof")
def proof_ephemeral():
    payload = f"AKSI-PROOF:{int(time.time())}".encode()
    digest = hashlib.sha256(payload).hexdigest()
    _log("proof_ephemeral", {"sha256": digest})
    return {"sha256": digest, "stable": False}

@app.post("/aksi/proof/stable")
def proof_stable():
    if PROOF_PATH.exists():
        digest = PROOF_PATH.read_text().strip()
        _log("proof_stable_read", {"sha256": digest})
        return {"sha256": digest, "stable": True}
    payload = f"AKSI-PROOF:seed:{int(time.time())}".encode()
    digest = hashlib.sha256(payload).hexdigest()
    PROOF_PATH.write_text(digest)
    _log("proof_stable_write", {"sha256": digest})
    return {"sha256": digest, "stable": True}

# --- Logs API ---
@app.get("/aksi/logs")
def logs_list(limit: int = 100):
    data = list(_logs)[-min(limit, LOG_CAP):]
    return {"items": data, "count": len(data), "cap": LOG_CAP}

@app.post("/aksi/logs/append")
async def logs_append(req: Request):
    body = await req.json() if req.headers.get("content-type","").startswith("application/json") else {"raw": await req.body()}
    _log("append", body if isinstance(body, dict) else {"raw": str(body)})
    return {"ok": True, "size": len(_logs)}

@app.get("/aksi/logs/export")
def logs_export():
    lines = [json.dumps(x, ensure_ascii=False) for x in _logs]
    return app.response_class(
        content='
'.join(lines),
        media_type="text/plain; charset=utf-8"
    )

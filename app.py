from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os, hashlib, time, pathlib

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

class Echo(BaseModel):
    data: dict

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"version": os.getenv("AKSI_VERSION", "0.1.0")}

@app.post("/echo")
def echo(payload: Echo):
    return payload.model_dump()

@app.get("/aksi/metrics")
def metrics():
    return {"ok": True, "ts": int(time.time()), "version": os.getenv("AKSI_VERSION", "0.1.0")}

# --- Proof: stable-on-disk within container (regenerates on new deploy) ---
PROOF_PATH = pathlib.Path("PROOF_SHA256.txt")

@app.get("/aksi/proof")
def proof_ephemeral():
    payload = f"AKSI-PROOF:{int(time.time())}".encode()
    return {"sha256": hashlib.sha256(payload).hexdigest(), "stable": False}

@app.post("/aksi/proof/stable")
def proof_stable():
    if PROOF_PATH.exists():
        return {"sha256": PROOF_PATH.read_text().strip(), "stable": True}
    payload = f"AKSI-PROOF:seed:{int(time.time())}".encode()
    digest = hashlib.sha256(payload).hexdigest()
    PROOF_PATH.write_text(digest)
    return {"sha256": digest, "stable": True}

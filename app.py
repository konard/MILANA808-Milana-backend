from fastapi import FastAPI
from pydantic import BaseModel
import os, hashlib, time

app = FastAPI(title="Milana Backend (AKSI)")

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

@app.get("/aksi/proof")
def proof():
    payload = f"AKSI-PROOF:{int(time.time())}".encode()
    return {"sha256": hashlib.sha256(payload).hexdigest()}

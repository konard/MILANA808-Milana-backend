from fastapi import FastAPI
from pydantic import BaseModel
import os

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

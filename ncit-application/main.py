from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/")
def root():
    return {"message": "FastAPI Backend is working", "status": 200}


@app.get("/health")
def health():
    return {"health": "health is good"}

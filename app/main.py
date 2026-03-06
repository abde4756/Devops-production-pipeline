from fastapi import FastAPI 
from datetime import datetime

app = FastAPI()

@app.get("/")
def root():
    return {"message": "ABDEL Devops Production API running"}

@app.get("/health")
def health():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}
from fastapi import FastAPI
import time
from datetime import datetime

start_time = time.time()
app = FastAPI()

@app.get("/health")
def health():
    return {
        "nama": "Tunas Bimatara Chrisnanta Budiman",
        "nrp": "5025231999",
        "status": "UP",
        "timestamp": datetime.now().isoformat(),
        "uptime": time.time() - start_time
    }
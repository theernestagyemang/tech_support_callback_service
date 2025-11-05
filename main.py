from fastapi import FastAPI, Request
import json
from datetime import datetime

app = FastAPI()

@app.post("/callback")
async def receive_callback(request: Request):
    data = await request.json()

    # Save callback data to file
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("callbacks.log", "a") as f:
        f.write(f"[{timestamp}] {json.dumps(data)}\n")

    return {
        "responseCode": "01",
        "responseMessage": "Callback received"
    }

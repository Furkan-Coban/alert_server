from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import time


app = FastAPI(title="Alert Server")

class Alert(BaseModel):
  camera_id: str
  track_id: str
  class_name: str
  event_type: str


@app.post("/alert")
def receive_alert(alert:Alert):
  timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
  print(f"[{timestamp}] ALARM [Camera: {alert.camera_id}]: "
          f"Object {alert.class_name} (ID: {alert.track_id}) "
          f"did '{alert.event_type}'")
  return {"status": "success", "received_data": alert}


if __name__ == "__main__":
    print("Starting FastAPI alert server on http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)
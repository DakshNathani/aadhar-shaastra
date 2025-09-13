from fastapi import FastAPI, UploadFile, File
import shutil
import os
from verification import verify_aadhaar_card

app = FastAPI(
    title="Aadhaar Verification API",
    description="API to verify Aadhaar QR, logo, and text extraction",
    version="1.0.0"
)

LOGO_PATH = "template.jpg"  # Aadhaar logo template

@app.get("/")
def home():
    return {"status": "Aadhaar Verification API running 🚀"}

@app.post("/verify/")
async def verify(file: UploadFile = File(...)):
    temp_file = f"temp_{file.filename}"
    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = verify_aadhaar_card(temp_file, LOGO_PATH)

    os.remove(temp_file)  # cleanup
    return result

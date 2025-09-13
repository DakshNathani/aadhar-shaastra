# Aadhaar Verification API 🔑

This API verifies Aadhaar cards by scanning **QR codes**, detecting the **Aadhaar logo**, and extracting Aadhaar numbers using **OCR**.

🚀 Base URL: [https://aadhar-shaastra.onrender.com](https://aadhar-shaastra.onrender.com)

---

## 📌 Endpoints

### 1. Health Check
Check if the API is running.

```http
GET /
Response

json
Copy code
{ "status": "Aadhaar Verification API running 🚀" }
2. Aadhaar Verification
Upload an Aadhaar card image to verify.

http
Copy code
POST /verify/
🔹 Request Parameters
file: Aadhaar card image (JPG, PNG, etc.)

📤 How to Send Requests
✅ Using cURL
bash
Copy code
curl -X POST "https://aadhar-shaastra.onrender.com/verify/" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@test.png"
✅ Using Python
python
Copy code
import requests

url = "https://aadhar-shaastra.onrender.com/verify/"
files = {"file": open("test.png", "rb")}
response = requests.post(url, files=files)

print(response.json())

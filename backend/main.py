from fastapi import FastAPI, UploadFile, File, Form
from services.ai_service import generate_summary
from services.email_service import send_email   # NEW IMPORT

app = FastAPI(title="Sales Insight Automator")

@app.get("/")
def home():
    return {"message": "API running successfully"}

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    email: str = Form(...)
):
    try:

        contents = await file.read()
        data = contents.decode("utf-8")

        summary = generate_summary(data)

        # NEW STEP → send email
        send_email(email, summary)

        return {
            "email": email,
            "summary": summary
        }

    except Exception as e:
        return {"error": str(e)}
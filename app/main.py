from fastapi import FastAPI

app = FastAPI(title="AI-Bino")


@app.get("/")
def home():
    return {
        "message": "AI-Bino is running",
        "status": "online"
    }
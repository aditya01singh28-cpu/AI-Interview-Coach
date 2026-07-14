from fastapi import FastAPI

app = FastAPI(
    title="Project Athena API",
    description="AI Powered Interview Coach",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Project Athena 🚀",
        "status": "Server Running",
        "developer": "Aditya Singh"
    }


@app.get("/health")
def health_check():
    return {
        "status": "Healthy",
        "message": "API is working perfectly!"
    }


@app.get("/about")
def about():
    return {
        "project": "Project Athena",
        "purpose": "AI Interview Coach",
        "backend": "FastAPI",
        "language": "Python"
    }
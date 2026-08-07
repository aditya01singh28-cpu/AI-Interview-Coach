from fastapi import FastAPI
from pydantic import BaseModel

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
#Empty list to store candidate data
candidates = []


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

@app.get("/greet/{name}")
def greet(name: str):
    return{
        "message": f"Hello {name}! Welcome to Project Athena 🚀"
    }

class Candidate(BaseModel):
    name: str
    role: str
    experience: str


@app.post("/candidate")
def create_candidate(candidate: Candidate):

    candidates.append(candidate)

    return {
        "message": "Candidate added successfully!",
        "total_candidates": len(candidates)
    }


@app.get("/candidates")
def get_candidates():
    return candidates

@app.put("/candidate/{name}")
def update_candidate(name: str, updated_candidate: Candidate):

    for candidate in candidates:

        if candidate.name.lower() == name.lower():

            candidate.name = updated_candidate.name
            candidate.role = updated_candidate.role
            candidate.experience = updated_candidate.experience

            return {
                "message": "Candidate updated successfully!",
                "candidate": candidate
            }

    return {
        "error": "Candidate not found"
    }
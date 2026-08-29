from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import engine, CandidateDB


app = FastAPI(
    title="Project Athena API",
    description="AI Powered Interview Coach",
    version="1.0.0"
)


class Candidate(BaseModel):
    name: str
    role: str
    experience: str


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
        "database": "PostgreSQL"
    }


@app.get("/greet/{name}")
def greet(name: str):
    return {
        "message": f"Hello {name}! Welcome to Project Athena 🚀"
    }


@app.post("/candidate")
def create_candidate(candidate: Candidate):

    db = Session(engine)

    new_candidate = CandidateDB(
        name=candidate.name,
        role=candidate.role,
        experience=candidate.experience
    )

    db.add(new_candidate)
    db.commit()
    db.refresh(new_candidate)
    db.close()

    return {
        "message": "Candidate added successfully!",
        "id": new_candidate.id
    }


@app.get("/candidates")
def get_candidates():

    db = Session(engine)

    candidates = db.query(CandidateDB).all()

    db.close()

    return candidates


@app.get("/candidate/{name}")
def get_candidate(name: str):

    db = Session(engine)

    candidate = db.query(CandidateDB).filter(
        CandidateDB.name.ilike(name)
    ).first()

    db.close()

    if candidate:
        return candidate

    return {
        "error": "Candidate not found"
    }


@app.delete("/candidate/{name}")
def delete_candidate(name: str):

    db = Session(engine)

    candidate = db.query(CandidateDB).filter(
        CandidateDB.name.ilike(name)
    ).first()

    if candidate:
        db.delete(candidate)
        db.commit()
        db.close()

        return {
            "message": f"{name} deleted successfully!"
        }

    db.close()

    return {
        "error": "Candidate not found"
    }


@app.put("/candidate/{name}")
def update_candidate(name: str, updated_candidate: Candidate):

    db = Session(engine)

    candidate = db.query(CandidateDB).filter(
        CandidateDB.name.ilike(name)
    ).first()

    if candidate:

        candidate.name = updated_candidate.name
        candidate.role = updated_candidate.role
        candidate.experience = updated_candidate.experience

        db.commit()
        db.refresh(candidate)
        db.close()

        return {
            "message": "Candidate updated successfully!",
            "candidate": candidate
        }

    db.close()

    return {
        "error": "Candidate not found"
    }
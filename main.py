from fastapi import FastAPI
import json

app = FastAPI()

with open("resume.json") as f:
    resume = json.load(f)


@app.get("/")
def home():
    return {
        "message": "Welcome to Mallik Resume API",
        "endpoint": "/resume"
    }


@app.get("/resume")
def get_resume():
    return resume


@app.get("/resume/skills")
def get_skills():
    return resume["skills"]


@app.get("/resume/experience")
def get_experience():
    return resume["experience"]


@app.get("/resume/projects")
def get_projects():
    return resume["projects"]


@app.get("/resume/contact")
def get_contact():
    return resume["contact"]

@app.get("/resume/education")
def get_education():
    return resume["education"]

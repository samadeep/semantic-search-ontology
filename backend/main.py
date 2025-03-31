# backend/main.py
from fastapi import FastAPI, Query
from typing import List
from ontology_loader import load_symptoms, load_conditions, load_links
from reasoning import infer_conditions

app = FastAPI()
symptoms = load_symptoms()
conditions = load_conditions()
links = load_links()

@app.get("/query")
def query(symptoms_query: List[str] = Query(...), age: int = 30, gender: str = "all"):
    results = infer_conditions(symptoms_query, age, gender, symptoms, conditions, links)
    return {"results": [{"condition": c.name, "score": s} for c, s in results]}

# README.md
# 🩺 Semantic Symptom Search (MVP)

This project demonstrates a semantic search engine for healthcare symptoms using a simplified ontology for Natural Language Processing - CS-442

## Features
- Accepts natural language symptom input as comma seperated format.
- Uses synonym mapping and ontology-based scoring
- Returns likely conditions with ranked relevance

## Project Structure
```
project-root/
├── backend/       # FastAPI-based inference service
├── frontend/      # Streamlit-based UI for testing
├── data/          # Ontology definitions in JSON
├── docker-compose.yml
├── Dockerfile.backend
├── Dockerfile.frontend
```

## Prerequisites
- Python 3.8+
- Docker (optional for container deployment)

## Setup Instructions (Manual)

### 1. Install Backend Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 2. Start Backend API
```bash
uvicorn main:app --reload --port 8000
```

### 3. Install Frontend Dependencies
```bash
cd ../frontend
pip install -r requirements.txt
```

### 4. Run Streamlit UI
```bash
streamlit run app.py
```

## Setup Instructions (Docker)

### 1. Build & Run with Docker Compose
```bash
docker-compose up --build
```

## Example Query
> Symptoms: `persistent cough, fatigue`  
> Age: `30`  
> Gender: `all`

Returns:
- Tuberculosis (Score: 1.30)
- Anemia (Score: 0.80)

## Data Format
JSON files under `data/` include:
- `symptoms.json`
- `conditions.json`
- `links.json`

These define how symptoms map to medical conditions.
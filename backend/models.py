
from pydantic import BaseModel
from typing import List, Optional, Dict

class Symptom(BaseModel):
    id: str
    name: str
    synonyms: List[str]

class Condition(BaseModel):
    id: str
    name: str
    description: str
    demographic_relevance: Dict[str, str]

class Link(BaseModel):
    symptom_id: str
    condition_id: str
    relationship_type: str
    weight: float
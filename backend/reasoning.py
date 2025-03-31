
from collections import defaultdict
from typing import List, Tuple
from models import Symptom, Condition, Link

def infer_conditions(query_symptoms: List[str], age: int, gender: str,
                     symptoms: List[Symptom], conditions: List[Condition], links: List[Link]) -> List[Tuple[Condition, float]]:

    matched_symptom_ids = set()
    for qs in query_symptoms:
        for sym in symptoms:
            all_terms = [sym.name.lower()] + [s.lower() for s in sym.synonyms]
            if qs.lower() in all_terms:
                matched_symptom_ids.add(sym.id)

    score_map = defaultdict(float)
    for link in links:
        if link.symptom_id in matched_symptom_ids:
            cond = next((c for c in conditions if c.id == link.condition_id), None)
            if cond and is_demographically_relevant(cond, age, gender):
                score_map[cond.id] += link.weight

    ranked = sorted(score_map.items(), key=lambda x: x[1], reverse=True)
    return [(next(c for c in conditions if c.id == cid), score) for cid, score in ranked]


def is_demographically_relevant(cond: Condition, age: int, gender: str) -> bool:
    ar = cond.demographic_relevance.get("age_range", "0-100")
    min_age, max_age = map(int, ar.split("-"))
    g = cond.demographic_relevance.get("gender", "all")
    return (min_age <= age <= max_age) and (g == "all" or g == gender.lower())
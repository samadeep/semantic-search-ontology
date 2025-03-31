import json
import os
from models import Symptom, Condition, Link

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def load_symptoms(path='data/symptoms.json'):
    full_path = os.path.join(BASE_DIR, path)
    return [Symptom(**item) for item in json.load(open(full_path))]

def load_conditions(path='data/conditions.json'):
    full_path = os.path.join(BASE_DIR, path)
    return [Condition(**item) for item in json.load(open(full_path))]

def load_links(path='data/links.json'):
    full_path = os.path.join(BASE_DIR, path)
    return [Link(**item) for item in json.load(open(full_path))]

import json
import os

DATA_DIR = "data"
FILE_PATH = os.path.join(DATA_DIR, "entries.json")

def save_entry(entries):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(FILE_PATH, "w") as file:
        json.dump(entries, file, indent=2)

def load_entries():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as file:
        return json.load(file)

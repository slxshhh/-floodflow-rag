import json
from app.services.ingestor import ingest_catalog

with open("data/sample_catalog.json", "r", encoding="utf-8") as file:
    content = json.load(file)

ingest_catalog(content)

import uuid
from app.core.database import get_vector_collection

def ingest_catalog(catalog_items):
    collection = get_vector_collection()
    documents = []
    metadatas = []
    ids = []
    for item in catalog_items:
        documents.append(str(item["content"]))
        metadatas.append(item["metadata"])
        id = str(uuid.uuid4())
        ids.append(id)
    collection.add(documents=documents, metadatas=metadatas, ids=ids)
    

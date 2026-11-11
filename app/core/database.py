import chromadb
from app.config import Settings

def get_chroma_client():
    settings = Settings()
    client = chromadb.PersistentClient(path=settings.CHROMA_PERSIST_DIR)
    return client


def get_vector_collection():
    settings = Settings()
    client = get_chroma_client()
    collection = client.get_or_create_collection(name=settings.COLLECTION_NAME)
    return collection
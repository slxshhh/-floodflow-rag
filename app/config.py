from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FloodFlow RAG"
    CHROMA_PERSIST_DIR: str = "./chroma_data"
    COLLECTION_NAME: str = "floodflow_catalog"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
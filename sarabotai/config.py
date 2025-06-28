import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Gemini API Configuration
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    
    # ChromaDB Configuration
    CHROMA_PERSIST_DIR = "./chroma_db"
    CHROMA_COLLECTION_NAME = "news_research"
    
    # Text Processing
    DEFAULT_CHUNK_SIZE = 1000
    DEFAULT_CHUNK_OVERLAP = 200
    
    # UI Settings
    MAX_URL_INPUTS = 3
    MAX_RESULTS = 5

from pathlib import Path
from langchain_chroma import Chroma
from rag.embeding import embeddings

BASE_DIR = Path(__file__).resolve().parent.parent
DB_DIR = BASE_DIR / "chroma-db"

vector_store = Chroma(
    embedding_function=embeddings,
    persist_directory=str(DB_DIR),
    collection_name="sample",
)

from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
KB_DIR = BASE_DIR / "KB"

documents=[]

for pdf_path in KB_DIR.rglob("*.pdf"):
    print(pdf_path)
    loader=PyPDFLoader(str(pdf_path))
    documents.extend(loader.load())



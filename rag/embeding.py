from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

embeddings=GoogleGenerativeAIEmbeddings(
    model="",
    api_key=os.getenv("GOOGLE_API_KEY"),
    output_dimensionality=768
)






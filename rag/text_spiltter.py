from langchain_text_splitters import RecursiveCharacterTextSplitter
from rag.loader import documents

splitter=RecursiveCharacterTextSplitter(
    chunk_size=2200,
    chunk_overlap=220,
     separators=[
        "\nfunc ",
        "\ntype ",
        "\n\n",
        "\n",
        " ",
        "",
    ],
)

chunks=splitter.split_documents(documents)
print("chunk size: ",len(chunks))
print(type(chunks))

from rag.vectorstore import vector_store

retriver = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 1,
        "lambda_mult": 0.5,
    },
)


# Run this only when testing this file directly
if __name__ == "__main__":
    print("Testing retriever...")

    result = retriver.invoke("CRUD with SQL and pgx")

    print(f"Retrieved documents: {len(result)}")

    for doc in result:
        print(doc.page_content[:1000])

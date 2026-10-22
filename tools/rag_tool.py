from langchain.tools import tool
from rag.retriver import retriver

@tool
def search_go_kb(query:str)->str:
    """Search personal Go programming PDFs for code examples,
    backend implementations, APIs, SQL, authentication,
    concurrency, and Go architecture.

    Use this tool when a question may be answered by the
    user's personal Go documentation or code examples.
    """
    try:
        documents=retriver.invoke(query)
        if not documents:
            return "No relevant information found in the Go knowledge base."

        results=[]
        for i,doc in enumerate(documents, start=1):
            source=doc.metadata.get("source","Unknown source")
            page=doc.metadata.get("page","Unknown")

            results.append(
                f"Result {i}\n"
                f"Source: {source}\n"
                f"Page: {page}\n"
                f"Content:\n{doc.page_content}"
            )
        return "\n\n---\n\n".join(results)
    
    except Exception:
        return (
            "The Go knowledge base search failed. "
            "Check the ChromaDB configuration and embedding API key."
        )


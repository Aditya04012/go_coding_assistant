
GO CODING ASSISTANT — WORKFLOW
================================

                 ┌──────────────────┐
                 │    User Query    │
                 └────────┬─────────┘
                          │
                 ┌────────▼─────────┐
                 │  FastAPI Backend │
                 └────────┬─────────┘
                          │
                 ┌────────▼─────────┐
                 │ LangChain Agent  │
                 │  (LLM + Tools)   │
                 └────────┬─────────┘
                          │
                 ┌────────▼─────────┐
                 │ Analyze Question │
                 └────────┬─────────┘
                          │
              ┌───────────┼────────────┐
              │           │            │
      ┌───────▼────┐ ┌────▼─────┐ ┌────▼─────────┐
      │ Personal KB│ │ Internet │ │   GitHub     │
      │    (RAG)   │ │  Search  │ │ Repo Search  │
      └───────┬────┘ └────┬─────┘ └────┬─────────┘
              │           │            │
      ┌───────▼────┐ ┌────▼─────┐ ┌────▼─────────┐
      │   Chroma   │ │ Search   │ │ GitHub API   │
      │ Vector DB  │ │   Tool   │ │ / Search Tool│
      └───────┬────┘ └────┬─────┘ └────┬─────────┘
              │           │            │
              └───────────┼────────────┘
                          │
                 ┌────────▼─────────┐
                 │ Combine Context  │
                 │ + User Question  │
                 └────────┬─────────┘
                          │
                 ┌────────▼─────────┐
                 │    LLM (Groq)    │
                 │ Reason + Generate│
                 └────────┬─────────┘
                          │
                 ┌────────▼─────────┐
                 │ Final Answer     │
                 │ Code + Explanation│
                 └──────────────────┘


PERSONAL KNOWLEDGE BASE — INDEXING PIPELINE
===========================================

 Your Go Projects / Source Files
              │
              ▼
       Load .go Files
              │
              ▼
       Split into Chunks
              │
              ▼
       Generate Embeddings
              │
              ▼
       Store in Chroma
              │
              ▼
       Personal Go Code KB
              │
              └──────────► Used by RAG Tool


TECH STACK
==========

- Language: Python
- API: FastAPI
- Agent / Workflow: LangChain create_agent()
- LLM: Groq
- Embeddings: HuggingFace
- Vector Database: Chroma
- Internet Search: Tavily or SerpAPI
- GitHub Search: GitHub API
- Knowledge Source: Your own Go repositories

NO LANGGRAPH REQUIRED
=====================

LangChain Agent + Tools + RAG






User Query
    |
FastAPI
    |
LangChain Agent
    |
Select Tools
    +---- Personal RAG (Chroma)
    +---- Internet Search
    +---- GitHub Search
    |
Combine Evidence
    |
Generate Go Code
    |
Run gofmt + go test
    |
  Tests pass?
    +---- No --> Repair Code --> Retry (limited)
    |
    Yes
    |
Answer + Sources + Code
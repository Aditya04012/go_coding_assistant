import time
from tools.rag_tool import search_go_kb

start = time.perf_counter()

result = search_go_kb.invoke({
    "query": "PGX sql in Golang"
})

print(result)
print(f"\nKB tool time: {time.perf_counter() - start:.2f} seconds")


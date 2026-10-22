import time
from agent.llm import llm

start = time.perf_counter()

response = llm.invoke("Explain Go middleware in 3 short lines.")

print(response.content)
print(f"LLM time: {time.perf_counter() - start:.2f} seconds")
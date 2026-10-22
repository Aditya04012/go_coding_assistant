from agent.assistant import assistant

response = assistant.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Simple sql implemtation in go pgx."
        }
    ]
})

answer = response["messages"][-1].content

if isinstance(answer, list):
    for block in answer:
        if block.get("type") == "text":
            print(block["text"])
else:
    print(answer)
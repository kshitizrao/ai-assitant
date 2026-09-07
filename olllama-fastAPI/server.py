from fastapi import FastAPI,Body
from ollama import Client
# from ollama import ChatResponse

app = FastAPI()
client = Client(
    host="http://localhost:11434"
) 


@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}

@app.post("/chat")
def chat(
    message: str= Body(..., description="The Message")
):
    response = client.chat(
        model="llama3.1",
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ]
    )

    return {"response": response.message.content}
    

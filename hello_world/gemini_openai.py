import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


response = client.chat.completions.create(
    model = "gemini-3.6-flash",
    messages = [
        {"role": "system", "content": "hey you are expert in maths, So only answer if the query is related to maths. Otherwise just reply by saying SORRY bro thats not maths"},
        {"role": "user", "content": "2+3+4+5+6+7+8+9"}
    ]
)

print(response.choices[0].message.content)
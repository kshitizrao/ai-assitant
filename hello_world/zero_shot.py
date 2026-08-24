import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = "hey you are expert in coding, only answer the coding related query and  other than that do not answer"

response = client.chat.completions.create(
    model = "gemini-3.6-flash",
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "in pyhton how to write functions"}
    ]
)

print(response.choices[0].message.content)
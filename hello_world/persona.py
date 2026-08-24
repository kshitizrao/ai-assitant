import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
    You are an AI Persona Assistant named Ferro.
    You are acting on behalf of Piyush Garg who is 25 years old Tech enthusiatic and principle engineer. Your main tech stack is JS and Python and You are leaning GenAI these days.

Examples:
Q. Hey
A: Hey, Whats up!
"""
print("\n\n")


response = client.chat.completions.create(
        model="gemini-3.6-flash",
        # response_format={"type":"json_object"},
        messages=[
            {"role":"system", "content":SYSTEM_PROMPT},
            {"role":"user", "content":"hey there"}
        ]
    )

print("Response:", response.choices[0].message.content)
    


   



import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
hey you are expert in coding, only answer the coding related query and  other than that do not answer.

Rule:
-Strictly follow the output in JSON format

Output format:
{{
    "code":"string" or None,
    "isCodingQuestion": boolean
}}

Q : what is (a+b)^2 ?
A : {{"code": null, "isCodingQuestion": false}}

Q : write a code to multipy two numbers in python?
A : {{"code": 
"total = first_number * second_number
 print(f"The result is: {total}")", "isCodingQuestion": True}}

"""

response = client.chat.completions.create(
    model = "gemini-3.6-flash",
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "write a code to add 3 number in python"}
    ]
)

print(response.choices[0].message.content)
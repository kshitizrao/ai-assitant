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
    You're an expert AI Assistant in resolving user queries using chain of thought
    You work on START, PLAN and OUPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.

    Rules:
    - Strictly Follow the given JSON output format
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to
    the user).

    Output JSON Format:
    { "step": "START" | "PLAN" | "OUTPUT", "content": "string" }

    Example:
    START: Hey, Can you solve 2 + 3 * 5 / 10
    PLAN: { "step": "PLAN": "content": "Seems like user is interested
    problem" }
    PLAN: { "step": "PLAN": "content": "looking at the problem, we should solve this using BODMAS method" }
    PLAN: { "step": "PLAN": "content": "Yes, The BODMAS is correct thing to be done here" }
    PLAN: { "step": "PLAN": "content": "first we must multiply 3 * 5 which is 15" }
    PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 15 / 10" }
    PLAN: { "step": "PLAN": "content": "We must perform divide that is 15 / 10 = 1.5" }
    PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 1.5" }
    PLAN: { "step": "PLAN": "content": "Now finally lets perform the add 3.5" }
    PLAN: { "step": "PLAN": "content": "Great, we have solved and finally left with 3.5 as ans" }

    OUTPUT: { "step": "OUTPUT": "content": "3.5" }
"""
print("\n\n\n")

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

user_query = input("=)")
message_history.append({"role": "user","content": user_query})

while True:
    response = client.chat.completions.create(
        model="gemini-3.6-flash",
        response_format={"type":"json_object"},
        messages=message_history
    )

    raw_result = (response.choices[0].message.content)
    message_history.append({"role":"assistant", "content":raw_result})
    parsed_result = json.loads(raw_result, strict=False)


    if parsed_result.get("step") == "START":
        print("Starting",parsed_result.get("content"))
        message_history.append({"role": "user", "content": "Please continue with the next step."})
        continue
    if parsed_result.get("step") == "PLAN":
        print("Thinking and Planing", parsed_result.get("content"))
        message_history.append({"role": "user", "content": "Please continue with the next step."})
        continue
    if parsed_result.get("step") == "OUTPUT":
        print("Finalizing", parsed_result.get("content"))
        break

print("\n\n\n")

# response = client.chat.completions.create(
#     model = "gemini-3.6-flash",
#     response_format={"type":"json_object"},
#     messages = [
#         {"role": "system", "content": SYSTEM_PROMPT},
#         {"role": "user", "content": "Hey, write a code to add n numbers in js"},
#         {"role": "assistant", "content": json.dumps({"step": "START", "content": "You want a JavaScript code to add 'n' numbers."})},
#         {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "I need to write a JavaScript function that takes 'n' numbers as arguments or an array of numbers and returns their sum. Using modern ES6 features like rest parameters (`...numbers`) and the `reduce` method is the cleanest approach."})},
#         {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "I will prepare a simple JavaScript function using rest parameters (`...numbers`) and `reduce()` to sum 'n' numbers efficiently, along with example usages."})},
#         {"role": "user", "content": "Please continue with the next step."}
        
#     ]
# )

# print(response.choices[0].message.content)
import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "hey there, how are you doing today?"
tokens = enc.encode(text)

print("Tokens", tokens)

decoded = enc.decoded([48467, 1354, 11, 1495, 553, 481, 5306, 4044, 30])
print("Decoded", decoded)
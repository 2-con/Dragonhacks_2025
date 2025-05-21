"""DOCSTRING
Dragonhacks competition 2025

Notes:
bassically chatgpt

"""

# imports

import openai

openai.api_key = "[DELETED]"

response = openai.chat.completions.create(
  model="GPT-3.5",
  messages=[
    {"role": "user", "content": "what is OCD?."},
  ]
)

print(response.choices[0].message.content)
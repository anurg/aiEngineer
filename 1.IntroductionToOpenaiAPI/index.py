import json
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
print(OPENAI_API_KEY)

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-5.4-mini",
    messages=[{"role":"user",
               "content":"Write a short poem on ai agents craze"}]
)

payload = json.dumps(response.model_dump(), indent=2, default=str)
print(payload)

with open("response.json", "w") as f:
    f.write(payload)
print(response.choices[0].message.content)



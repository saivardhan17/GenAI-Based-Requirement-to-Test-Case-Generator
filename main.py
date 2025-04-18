import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

requirement_input = input("Enter your requirement: ")

prompt = f"""
You are a software architect assistant.

Convert the following software requirement into:

1. A list of 3-5 functional requirements
2. 2-3 non-functional requirements
3. Gherkin-style test cases
4. A basic sequence diagram description in PlantUML syntax

Requirement:
\"\"\"{requirement_input}\"\"\"
"""

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.4,
    max_tokens=1000
)

print("\n🧠 Generated Output:")
print(response.choices[0].message.content)

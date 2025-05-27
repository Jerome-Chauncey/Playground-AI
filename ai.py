import os
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())

from openai import OpenAI

# Access API key after loading .env
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

messages = [{"role": "user", "content": "What is the capital of New York?"}]
try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0
    )
    print(response.choices[0].message.content)
except Exception as e:
    print("Error:", e)

import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv(dotenv_path="../.env")

AI_API_KEY = os.getenv("OPEN_AI_KEY")

# role of the AI assistant
role = "You are a skilled cook with the expertise of a chef as well as a graduate dietician"

# instanciate the object
client = OpenAI(api_key=AI_API_KEY)

# Prompt
prompt = "Tell me what calories an adult of 34 years that wants to get to 90kg but wants to have muscles and be lean needs to have every day. The adult is a man of 1,75 kg and does sport 4 times a week"

def generate_response():
    response = client.chat.completions.create(
        model = "gpt-5-nano-2025-08-07",
        messages = [
            {"role":"system", "content": role},
            {"role":"user", "content":prompt}
        ]
    )

    return response.choices[0].message.content

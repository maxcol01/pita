import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv(dotenv_path="../.env")

AI_API_KEY = os.getenv("OPEN_AI_KEY")

# role of the AI assistant
role = "You are a skilled cook with the expertise of a chef as well as a graduate dietitian"

# instance the object
client = OpenAI(api_key=AI_API_KEY)

# format the ingredient from the db into string (python list to string content)
def format_ingredients_for_prompt(items):
    lines = []
    for item in items:
        lines.append(
            f"- {item['name']} ({item['quantity']} {item['unit']})"
        )
    return "\n".join(lines)

# Prompt
prompt = f"""
        Your task is to generate ONE simple, healthy recipe using the ingredients provided below.
        
        ### Available pantry ingredients:
        ```{{ingredients}}```
        
        Salt, pepper, and common spices are ALWAYS allowed and do not need to be listed.
        
        You MAY add additional ingredients ONLY if necessary to make the recipe coherent, tasty, or nutritionally balanced.
        
        ### Rules:
        1. Use as many pantry ingredients as possible.
        2. Clearly separate ingredients already available from ingredients that must be purchased.
        3. Specify exact quantities for ALL ingredients.
        4. Keep the recipe simple and realistic.
        5. The recipe should be suitable for everyday home cooking.
        6. Output MUST be valid JSON and NOTHING ELSE (no explanations, no markdown).
        
        ### Example of JSON Output Format:
        {{
          "title": "Concise recipe title (also suitable as a DALL·E prompt)",
          "description": "Short description of the dish",
          "servings": 1,
          "calories": <integer>,
          "time": {{
            "prep_minutes": <integer>,
            "cook_minutes": <integer>,
            "total_minutes": <integer>
          }},
          "ingredients_used": [
            {{
              "name": "ingredient name",
              "quantity": "exact quantity",
              "source": "pantry"
            }}
          ],
          "ingredients_to_buy": [
            {{
              "name": "ingredient name",
              "quantity": "exact quantity"
            }}
          ],
          "steps": [
            "Step 1 description",
            "Step 2 description",
            "Step 3 description"
          ]
        }}
        FINAL CHECK (MANDATORY):
        If an ingredient name is not an EXACT STRING MATCH with the pantry list,
        it MUST NOT appear in "ingredients_used".
"""

def generate_response():
    response = client.chat.completions.create(
        model = "gpt-5-nano-2025-08-07",
        messages = [
            {"role":"system", "content": role},
            {"role":"user", "content":prompt}
        ]
    )

    return response.choices[0].message.content

import requests
import os
from dotenv import load_dotenv

load_dotenv()
HF_API_KEY = os.getenv("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")

API_URL = "API_URL = "https://api-inference.huggingface.co/models/gpt2"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def get_bot_response(user_input):
    output = query({"inputs": user_input})
    try:
        return output['generated_text']
    except:
        return "Sorry, I didn't get that. Please try again."

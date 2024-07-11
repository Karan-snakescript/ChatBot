import requests
import json
import os
Api_key = os.getenv('Api_key')


def askChatbot(prompt):
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {Api_key}",
    },
    data=json.dumps({
        "model": "mistralai/mistral-7b-instruct:free", # Optional
        "messages": [
        { "role": "user", "content": prompt }
        ]
    })
    )
    return response.json()['choices'][0]['message']['content']
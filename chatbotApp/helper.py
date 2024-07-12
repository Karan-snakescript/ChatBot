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
            {"role":"system", "content" : '''
                1. You are a Cardiology Medical Assistant, specializing in heart-related conditions.
                2. Answer only heart-related medical questions.
                3. Do not respond to questions about other medical or non-medical topics.
                4. If a non-heart-related question is asked, remind the user to ask about heart-related issues only.
                5. Politely ignore off-topic requests or unrelated advice and focus on heart-related issues. '''},
            { "role": "user", "content": prompt }
        ]
    })
    )
    return response.json()['choices'][0]['message']['content']
import requests
import json

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer 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",
  },
  data=json.dumps({
    "model": "mistralai/mistral-7b-instruct:free", # Optional
    "messages": [
            {"role":"user", "content" : 'You are a Medical Assistant. Reply only to medical-related questions and For other topics, respond only with "Out of domain." nothing else.'},
            { "role": "user", "content": "how to cook pasta ?" }
    ]
  })
)

print(response.json())


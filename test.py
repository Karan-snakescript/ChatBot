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
      { "role": "user", "content": "What is the meaning of life?" }
    ]
  })
)

print(response.json())


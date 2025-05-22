import requests
import os
import json

# Get API key from environment variable
API_KEY = '0a26ee7b-3bca-42ac-93cf-9bfc97fb70e8'

# Constants / placeholders
url = "https://egp.dashboard.scale.com/api/v4/applications/2ee05581-6dfc-4580-9b0f-345e9741a135/process"

payload = {
    "inputs": {
        "knowledge_base_ids": [
            "9947842f-ddd7-4a73-b2c0-227c79e22871"
        ],
        "query": "Pruning"
    }
}

headers = {
    'x-api-key': API_KEY
}

response = requests.post(
    url,
    json=payload,
    headers=headers
)

print(f"Message: {json.loads(response.json()['message']['content'])['llm']}")

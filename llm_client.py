import requests

def call_llm(prompt):
    url = "http://127.0.0.1:8000/generate"

    response = requests.post(url, json={
        "prompt": prompt,
        "model": "mistral"
    })

    return response.json()["response"]
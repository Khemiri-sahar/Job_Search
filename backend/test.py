import requests

response = requests.post(
    "http://127.0.0.1:8000/recommend",
    json={"text": "Python developer", "top_k": 3}
)

print("Status:", response.status_code)
print("Results:", response.json())
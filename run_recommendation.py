import requests

url = "http://127.0.0.1:8000/recommend"

patient_info = {
    "gender": "female",
    "age": 62,
    "symptoms": ["pusing", "mual", "sulit berjalan"]
}

try:
    response = requests.post(url=url, json=patient_info)
    print(response.json(), end='')
except Exception as e:
    print(f"Error: str{e}")
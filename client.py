import requests

url = "http://localhost:8000/predict"

# Define request payload
payload = {
    "prompt": "Melodic human whistling harmonizing with natural birdsong",
    "duration": 10,
}

# Send request
response = requests.post(url, json=payload)

# Save the received audio file
with open("output.wav", "wb") as f:
    f.write(response.content)

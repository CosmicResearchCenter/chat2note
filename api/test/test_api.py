import requests

data = {
  "url": "https://chatgpt.com/share/670d07c5-7760-8009-9d55-91dbac44a1fb",
  "steaming": True
}

url = "http://127.0.0.1:9988/v1/api/chat2note/chat2note"
with requests.post(url=url, json=data, stream=True) as response:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            print(chunk)
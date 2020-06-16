#"/send"
#{"username": "", "text": ""}

import requests

response = requests.get("http://127.0.0.1:5000/status")
print(response.text)

print("Enter your name")
username = input()
print("Enter your password")
password = input()

response = requests.post(
    "http://127.0.0.1:5000/auth",
    json={"username": username, "password": password}
)
if not response.json()['ok']:
    print('Wrong password')
    exit()

while True:
    print(username, "Enter message:")
    text = input()
    response = requests.post("http://127.0.0.1:5000/send", json={"username": username, "password": password, "text": text})
    print()
    #print(response.text)
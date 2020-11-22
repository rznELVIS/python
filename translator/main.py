import requests

URL_AUTH: str = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE: str = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY: str = 'Y2Y2YmYyZGItMmIyMS00MGY2LWIzNzItOWUwM2M4ZjY2NjBkOjEyMDE4NWE3NmJjYzRhMjdhYzEwOTk4Nzg4NTQ3ZGFm'

headers_auth = {'Authorization': 'Basic ' + KEY}

auth = requests.post(URL_AUTH, headers=headers_auth)

print(auth.status_code)
print(auth.text)

print("Hello translator!")

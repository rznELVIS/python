import requests

URL_AUTH: str = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE: str = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY: str = 'Y2Y2YmYyZGItMmIyMS00MGY2LWIzNzItOWUwM2M4ZjY2NjBkOjEyMDE4NWE3NmJjYzRhMjdhYzEwOTk4Nzg4NTQ3ZGFm'

headers_auth = {'Authorization': 'Basic ' + KEY}

auth = requests.post(URL_AUTH, headers=headers_auth)

if auth.status_code == 200:
    token = auth.text
    while True:
        word = input('Введите слово:')
        if word:
            headers_translate = {
                'Authorization': 'Bearer ' + token
            }
            params = {
                'text': word,
                'srcLang': 1033, #English
                'dstLang': 1049 #Rissian
            }
            requestTranslate = requests.get(
                URL_TRANSLATE,
                headers=headers_translate,
                params=params)
            result = requestTranslate.json()
            try:
                print('Перевод:' + result['Translation']['Translation'])
            except:
                print('Не найден перевод.')
else:
    print('auth error!')

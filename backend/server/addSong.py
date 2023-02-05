import requests
'''
f = open('token.json')
data = json.load(f)

for i in data:
    if i == 'token_type':
        token_type = data[i]
    if i == 'access_token':
        access_token = data[i]
'''
A='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjJhNzU4ZTk5OGE1Mzc0ZTkzMjU0ZGUzNjU0YWI2Njk3NTk3N2JhZmRlYjQ3YWFmMjQ4YjEyZTNiYWM4MWUwMDBhYzExYjdlOWNjYjdhYzAyIn0.eyJhdWQiOiJjYjFlODQ3ZjJhYTVkOTJmYTcwNDRlN2EyZmEzYjg0OCIsImp0aSI6IjJhNzU4ZTk5OGE1Mzc0ZTkzMjU0ZGUzNjU0YWI2Njk3NTk3N2JhZmRlYjQ3YWFmMjQ4YjEyZTNiYWM4MWUwMDBhYzExYjdlOWNjYjdhYzAyIiwiaWF0IjoxNjc1NTg4MjI4LCJuYmYiOjE2NzU1ODgyMjgsImV4cCI6MTY3ODAwNzQyOCwic3ViIjoiMTYyNTc2NzkiLCJzY29wZXMiOltdfQ.iEOQKqX_zZETtUSnhDtb8mzGOu6uSsAgGdosaMIf6lyO_k0XvyuNjMHa4St1IuSW5MR7atkcX8tcw2dY_MZ9_WMP5yusu_9EYz86kfOlz6O4pPcR5-yoIKWePzgZLG1Qifmylh5dUlPyqzCv9oyGO7V4IU35kcdcRP8_7GFauUjqalA97jX6-VDqTbNkKRJaj5s8S8AaWgN43uzJ1NVL2zh-0F5BkpI8tuT07EiPKo-n9VoKBWB-11XzF8O_t2vPf6b82gmE41aIbq9uiCRwxVG-kcuRfp6aBhME_VscwQjNLEz6WG4yA38NTyglqSBfcaJYZYQJ5bMDjCmGztqBiA'

header={'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': A,
        'User Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
id={'X-MAL-CLIENT-ID': 'cb1e847f2aa5d92fa7044e7a2fa3b848'}
data = {
    'status': 'watching'
}

#url = "https://api.myanimelist.net/v2/users/@me"

#r = requests.delete('https://api.myanimelist.net/v2/anime/29803/completed', headers=header)
#r = requests.get('https://api.myanimelist.net/v2/users/@me',headers=header)
r = requests.patch('https://api.myanimelist.net/v2/anime/17074/my_list_status',headers=header,data=data)
#r = requests.get('https://api.myanimelist.net/v2/users/Longinus11/animelist?status=watching', headers=id)
print(r)
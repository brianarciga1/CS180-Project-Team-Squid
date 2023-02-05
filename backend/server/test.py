from scrape import UrlManager
from mal import AnimeSearch
import requests
import json
import secrets

client_id = 'cb1e847f2aa5d92fa7044e7a2fa3b848'
CLIENT_SECRET = '9e9f3e0112ca5cc3e5376f6205196ffb250d736c4e1deb9d8968057f339ad392'


# 1. Generate a new Code Verifier / Code Challenge.
def get_new_code_verifier() -> str:
    token = secrets.token_urlsafe(100)
    return token[:128]

def print_new_authorisation_url(code_challenge: str):
    global client_id

    url = f'https://myanimelist.net/v1/oauth2/authorize?response_type=code&client_id={client_id}&code_challenge={code_challenge}&state=RequestID42'
    print(f'Authorise your application by clicking here: {url}\n')

# 3. Once you've authorised your application, you will be redirected to the webpage you've
#    specified in the API panel. The URL will contain a parameter named "code" (the Authorisation
#    Code). You need to feed that code to the application.
def generate_new_token(authorisation_code: str, code_verifier: str) -> dict:
    global client_id, CLIENT_SECRET

    url = 'https://myanimelist.net/v1/oauth2/token'
    data = {
        'client_id': client_id,
        'client_secret': CLIENT_SECRET,
        'code': authorisation_code,
        'code_verifier': code_verifier,
        'grant_type': 'authorization_code'
    }

    response = requests.post(url, data)
    response.raise_for_status()  # Check whether the request contains errors

    token = response.json()
    response.close()
    print('Token generated successfully!')

    with open('token.json', 'w') as file:
        json.dump(token, file, indent = 4)
        print('Token saved in "token.json"')

    return token


# 4. Test the API by requesting your profile information
def print_user_info(access_token: str):
    url = 'https://api.myanimelist.net/v2/users/@me'
    response = requests.get(url, headers = {
        'Authorization': f'Bearer {access_token}'
        })
    
    response.raise_for_status()
    user = response.json()
    response.close()

    print(f"\n>>> Greetings {user['name']}! <<<")

'''
url = "https://www.crunchyroll.com/watch/GRMGQX55R/izuku-midoriya-origin"
url1 ="https://www.crunchyroll.com/watch/G4VUQZ7MX/the-new-threat"
url2 = "https://tubitv.com/tv-shows/395405/s01-e01-end-and-beginning?start=true"

url_manager = UrlManager()
url_manager.add_new_url(url1)
resualt = url_manager.search(url_manager.get_url())

ID = AnimeSearch(resualt[0][7:]).results[0].mal_id

header = {'X-MAL-CLIENT-ID': client_id}

r = requests.get("https://api.myanimelist.net/v2/users/Longinus11/animelist?status=watching",headers=header)
print(r.text)
'''

if __name__ == '__main__':
    code_verifier = code_challenge = get_new_code_verifier()
    print_new_authorisation_url(code_challenge)

    authorisation_code = input('Copy-paste the Authorisation Code: ').strip()
    token = generate_new_token(authorisation_code, code_verifier)

    print_user_info(token['access_token'])

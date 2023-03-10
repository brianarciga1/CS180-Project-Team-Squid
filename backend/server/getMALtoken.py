import requests
import json
import secrets
from flask import session, request

client_id = 'cb1e847f2aa5d92fa7044e7a2fa3b848'
CLIENT_SECRET = '9e9f3e0112ca5cc3e5376f6205196ffb250d736c4e1deb9d8968057f339ad392'

class getMALtoken():
    
    # 1. Generate a new Code Verifier / Code Challenge.
    def get_new_code_verifier(self) -> str:
        token = secrets.token_urlsafe(100)
        return token[:50]

    def print_new_authorisation_url(self,code_challenge: str):
        global client_id
        
        url = f'https://myanimelist.net/v1/oauth2/authorize?response_type=code&client_id={client_id}&code_challenge={code_challenge}&state=RequestID42'
        return url

    # 3. Once you've authorised your application, you will be redirected to the webpage you've
    #    specified in the API panel. The URL will contain a parameter named "code" (the Authorisation
    #    Code). You need to feed that code to the application.
    def generate_new_token(self,authorisation_code: str, code_verifier: str) -> dict:
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

        return token


    # 4. Test the API by requesting your profile information ***
    def print_user_info(self,access_token: str):
        url = 'https://api.myanimelist.net/v2/users/@me'
        response = requests.get(url, headers = {
            'Authorization': f'Bearer {access_token}'
            })
        
        response.raise_for_status()
        user = response.json()
        response.close()

        print(f"\n>>> Greetings {user['name']}! <<<")
    
    # We only need to run this function to get the token, remember to delete 'token.json' before running this funcion
    # only the string after 'code=' and before '&status'
    # 1 remaining question: how can we get the code from the browser?
    # let the user copy and paste it?
    def get_token(self):

        if request.args.get("code"):
            code_verifier = session['code_verifier']
            authorisation_code = request.args.get("code")
            token = self.generate_new_token(authorisation_code, code_verifier)
            session['mal_token'] = token
            return 'auth complete'
        
        code_verifier = code_challenge = self.get_new_code_verifier()
        session['code_verifier'] = code_verifier
        url = self.print_new_authorisation_url(code_challenge)
        return f'<h2><a href="{url}">Sign in</a></h2>'

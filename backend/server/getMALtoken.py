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

import requests
import json

class addSong():
    def __init__(self) -> None:
        self.token_type = ""
        self.access_token = ""
        
    def open_token(self):
        f = open('.cache')
        data = json.load(f)

        for i in data:
            if i == 'token_type':
                self.token_type = data[i]
            if i == 'access_token':
                self.access_token = data[i] 
                
    def create_list(self):
        headers = {
            'Authorization': self.token_type + ' ' + self.access_token
            ,'Content-Type': 'application/json',
        }

        data = {
            'name': 'MAPL',
            'description': 'MAPL',
            'public': False,
        }

        response = requests.get('https://api.spotify.com/v1/me', headers=headers)
        print(json.dump(response.text)['id'])

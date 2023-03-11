import spotipy
from flask import session
import requests
import json
from spotipy.oauth2 import SpotifyOAuth

class addSong():
    def __init__(self) -> None:
        self.token_type = "Bearer "
        self.access_token = ""
        self.userID = ""
        self.playlistID = ''
        
    # get the token from '.cache'
    # must run this function first
    def open_token(self):
        data = session['token_info']

        for i in data:
            if i == 'access_token':
                self.access_token = data[i] 
                
    # must run this function second, after open_token
    def create_list(self, name, description):
        headers = {
            'Authorization': self.token_type + self.access_token,
            'Content-Type': 'application/json'
        }

        data = '{\n  "name": "' + name + '",\n  "description": "' + description + '",\n  "public": true\n}'
        response = requests.get('https://api.spotify.com/v1/me', headers=headers)
        self.userID = (json.loads(response.text)['id'])
        
        response = requests.post('https://api.spotify.com/v1/users/'+self.userID+'/playlists', headers=headers, data=data)
        self.playlistID = (json.loads(response.text)['id'])
        return self.playlistID

    def add_to_list(self, lists):
        headers = {
            'Authorization': self.token_type + self.access_token,
            'Content-Type': 'application/json'
        }

        my_uri = {"uris" : lists[0:99]}
        data = json.dumps(my_uri)
        response = requests.post('https://api.spotify.com/v1/playlists/' + self.playlistID +'/tracks', headers=headers, data=data)
        print('good')
        
        
    # search all the OPs and EDs
    # results is the superlist, each element is a list of animes
    # results[index] is also a superlist, each element contains all OPs and EDs of an anime
    # results[index][0] is the name of the song, [1] is the uri of the song used for add_Song
    def search(self,lists:list):
        headers = {
            'Authorization': self.token_type + ' ' + self.access_token
            ,'Content-Type': 'application/json'
        }
        results = []

        for i in lists:
            nameAnduri = []
            r = requests.get('https://api.spotify.com/v1/search?q='+i+'&type=track', headers=headers)
            nameAnduri.append(json.loads(r.text)['tracks']['items'][0]['name'])
            nameAnduri.append(json.loads(r.text)['tracks']['items'][0]['uri'])
            results.append(nameAnduri)
        
        return results
    
    # add each song to the list 'MAPL'
    def add_Song(self,lists:list):
        headers = {
            'Authorization': self.token_type + ' ' + self.access_token
            ,'Content-Type': 'application/json'
        }
        for anime in lists:
            data = '{\n  "uris": [\n    "'+anime[1]+'"\n  ],\n  "position": 0\n}'
            response = requests.post('https://api.spotify.com/v1/playlists/'+self.playlistID+'/tracks', headers=headers, data=data)
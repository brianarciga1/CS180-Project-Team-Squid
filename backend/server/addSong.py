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
            resultofAnime = []
            for j in i:
                nameAnduri = []
                r = requests.get('https://api.spotify.com/v1/search?q='+j+'&type=track', headers=headers)
                nameAnduri.append(json.loads(r.text)['tracks']['items'][0]['name'])
                nameAnduri.append(json.loads(r.text)['tracks']['items'][0]['uri'])
                resultofAnime.append(nameAnduri)
            results.append(resultofAnime)
        
        return results
    
    # add each song to the list 'MAPL'
    def add_Song(self,lists:list):
        headers = {
            'Authorization': self.token_type + ' ' + self.access_token
            ,'Content-Type': 'application/json'
        }
        for anime in lists:
            for song in anime:
                data = '{\n  "uris": [\n    "'+song[1]+'"\n  ],\n  "position": 0\n}'
                response = requests.post('https://api.spotify.com/v1/playlists/'+self.playlistID+'/tracks', headers=headers, data=data)
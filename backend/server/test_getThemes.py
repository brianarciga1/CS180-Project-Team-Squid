import unittest
from addSong import addSong
import json
import requests
from getThemes import getThemes

class TestgetThemes(unittest.TestCase):
    def setUp(self):
        self.testGetThemes = getThemes()
        self.testAddSong = addSong()
        f = open('tokens.json')
        data = json.load(f)
        self.testGetThemes.access_token = data["mal_token"]
        self.testAddSong.access_token = data["sp_token"]
        f.close()
        
        self.headers = {
            'Authorization': self.testAddSong.token_type + self.testAddSong.access_token,
            'Content-Type': 'application/json'
        }
        self.playlistID = ""
        
    # create a list "testCase4" and add one song in it by get_themes, "STAND PROUD"
    def test_get_themes(self):
        form = {'playlistTitle': 'testCase4', 'playlistDesc': 'testCase4', 'listOptions': ['watching'], 'songTypes': ['op']}
        self.playlistID = self.testAddSong.create_list("testCase4", "testCase4")
        response = requests.get('https://api.spotify.com/v1/playlists/'+self.playlistID, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        
        tmp = self.testGetThemes.get_themes(form, self.testAddSong)
        response = requests.get('https://api.spotify.com/v1/playlists/'+self.playlistID+'/tracks', headers=self.headers)
        self.assertEqual(response.status_code, 200)
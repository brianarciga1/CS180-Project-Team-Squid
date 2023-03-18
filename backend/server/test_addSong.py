import unittest
from addSong import addSong
import json
import requests

class TestaddSong(unittest.TestCase):     
    def setUp(self):
        self.testAddSong = addSong()
        f = open('tokens.json')
        data = json.load(f)
        self.testAddSong.access_token = data["sp_token"]
        f.close()
        
        self.headers = {
            'Authorization': self.testAddSong.token_type + self.testAddSong.access_token,
            'Content-Type': 'application/json'
        }
        self.playlistID = ""
    
    # create an empty list "testCase1"
    def test_create_list(self):
        self.playlistID = self.testAddSong.create_list("testCase1", "testCase1")
        response = requests.get('https://api.spotify.com/v1/playlists/'+self.playlistID, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        
    # create a list "testCase2" and add one song in it by add_to_list, "STAND PROUD"
    def test_add_to_list(self):
        self.playlistID = self.testAddSong.create_list("testCase2", "testCase2")
        response = requests.get('https://api.spotify.com/v1/playlists/'+self.playlistID, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        
        data = ['spotify:track:1YTW2IiSDH0buMd07A5Nnw']
        self.testAddSong.add_to_list(data)
        response = requests.get('https://api.spotify.com/v1/playlists/'+self.playlistID+'/tracks', headers=self.headers)
        self.assertEqual(response.status_code, 200)
    
    # search for "STAND PROUD"
    def test_search(self):
        data = ["STAND PROUD"]
        self.assertEqual((self.testAddSong.search(data))[0][0], "STAND PROUD")
    
    # create a list "testCase3" and add one song in it by add_Song, "STAND PROUD"
    def test_add_Song(self):
        self.playlistID = self.testAddSong.create_list("testCase3", "testCase3")
        response = requests.get('https://api.spotify.com/v1/playlists/'+self.playlistID, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        
        data = ["STAND PROUD"]
        list = self.testAddSong.search(data)
        self.testAddSong.add_Song(list)
        
        response = requests.get('https://api.spotify.com/v1/playlists/'+self.playlistID+'/tracks', headers=self.headers)
        self.assertEqual(response.status_code, 200)
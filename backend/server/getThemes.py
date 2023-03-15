from flask import session, request
from random import randint
from bs4 import BeautifulSoup
import time
import requests
import json

class getThemes():
    def __init__(self):
        self.token_type = "Bearer "
        self.access_token = ""
    
    # get the token from 'token.json', must run this first
    def open_token(self):
        data = session['mal_token']

        for i in data:
            if i == "access_token":
                self.access_token = data[i]  

    # get the themes
    # animeThemes is a list of animes(list): 0 = anime0, 1 = anime1...
    # inside the sublist(animes0), it contains all the OPs and EDs
    # OP and ED string: name 'by' author
    def get_themes(self,form,add_Song):
        header={'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': self.token_type + self.access_token,
        'User Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
        animeIDs = []
        path1 = 'https://api.myanimelist.net/v2/users/@me/animelist'
        status = '?status='
        limit = '&limit=1000'
        if len(form['listOptions']) < 5:
            for i in range(len(form['listOptions'])):
                newstatus = status + form['listOptions'][i] 
                newpath = path1 + newstatus
                r = requests.get(newpath + limit, headers=header)
                #r = requests.get(newpath, headers=header)
                for i in json.loads(r.text)['data']:
                    animeIDs.append(i['node']['id'])
        else:
            r = requests.get(path1, headers=header)
            for i in json.loads(r.text)['data']:
                animeIDs.append(i['node']['id'])
        header={'Content-Type': 'application/x-www-form-urlencoded',
        'User Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
        numAni = 0
        songID=[]
        animeThemes=[]
        fields = '?fields='
        check_op = False
        check_ed = False
        for i in range(len(form['songTypes'])):
            if form['songTypes'][i] == 'op':
                check_op = True
            if form['songTypes'][i] =='ed':
                check_ed = True
        for i in animeIDs:
            site = requests.get('https://myanimelist.net/anime/' + str(i), headers=header)
            numAni +=1
            print(numAni)
            soup = BeautifulSoup(site.text, 'lxml')
            ops_div = soup.find('div', class_ = 'theme-songs js-theme-songs opnening')
            eds_div = soup.find('div', class_ = 'theme-songs js-theme-songs ending')
            songs = []
            if check_op:
                songs += ops_div.findAll('input')
            if check_ed:
                songs += eds_div.findAll('input')
            for song in songs:
                if 'spotify' in song['id'] and song['value'] != '':
                    songID.append('spotify:track:' + song['value'][31:])
                elif 'spotify' in song['id']:
                    song_parent = song.parent
                    song_artist = song_parent.find('span', class_ = 'theme-song-artist')
                    if len(song_parent.contents[0].string) > 2:
                        songTitle = song_parent.contents[0].string
                    else:
                        songTitle = song_parent.contents[1][1:]
                    if song_artist is None:
                        continue
                    song_artist = song_artist.string
                    animeThemes.append(songTitle + song_artist) 
            time.sleep(randint(1,5))

        add_Song.add_to_list(songID)
            
            
        return animeThemes
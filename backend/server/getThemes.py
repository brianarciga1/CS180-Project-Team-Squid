from flask import session, request
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
    def get_themes(self,form):
        header={'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': self.token_type + self.access_token,
        'User Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
        animeIDs = []
        path1 = 'https://api.myanimelist.net/v2/users/@me/animelist'
        status = '?status='
        if len(form['listOptions']) < 5:
            for i in range(len(form['listOptions'])):
                newstatus = status + form['listOptions'][i] 
                newpath = path1 + newstatus
                r = requests.get(newpath, headers=header)
                for i in json.loads(r.text)['data']:
                    animeIDs.append(i['node']['id'])
        else:
            r = requests.get(path1, headers=header)
            for i in json.loads(r.text)['data']:
                animeIDs.append(i['node']['id'])
        
        animeOPED=[]
        animeThemes=[]
        fields = '?fields='
        for i in range(len(form['songTypes'])):
            if i != 0:
                fields += ','
            if form['songTypes'][i] == 'op':
                fields += 'opening_themes'
            if form['songTypes'][i] =='ed':
                fields += 'ending_themes'
        for i in animeIDs:
            response =requests.get("https://api.myanimelist.net/v2/anime/"+str(i)+"?fields=opening_themes,ending_themes", headers=header)
            rJSON = json.loads(response.text)
            if rJSON['opening_themes']:
                for i in rJSON['opening_themes']:
                    if i['text'][0] =='#':
                        animeOPED.append(i['text'][4:])
                    else:
                        animeOPED.append(i['text'])
            else:
                animeOPED.append('No Opening')
            if rJSON['ending_themes']:
                for i in rJSON['ending_themes']:
                    if i['text'][0] =='#':
                        animeOPED.append(i['text'][4:])
                    else:
                        animeOPED.append(i['text'])
            else:
                animeOPED.append('No Ending')
            animeThemes.append(animeOPED)
            animeOPED = []
            
        return animeThemes
import requests
import json

class addAnime():
    def __init__(self):
        self.token_type = ""
        self.access_token = ""
    
    def open_token(self):
        f = open('token.json')
        data = json.load(f)

        for i in data:
            if i == 'token_type':
                self.token_type = data[i]
            if i == 'access_token':
                self.access_token = data[i]  

    def addAnime(self,ID=list):
        header={'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': self.token_type +' '+ self.access_token,
        'User Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

        data = {
        'status': 'watching'
        }
        for id in ID:
            r = requests.patch('https://api.myanimelist.net/v2/anime/'+str(id)+'/my_list_status',headers=header,data=data)

    def get_op_ed(self):
        header={'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': self.token_type +' '+ self.access_token,
        'User Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
        ids = []
        r = requests.get('https://api.myanimelist.net/v2/users/@me/animelist?status=watching', headers=header)
        for i in json.loads(r.text)['data']:
            ids.append(i['node']['id'])
        
        ops=[]
        eds=[]
        for i in ids:
            op =requests.get("https://api.myanimelist.net/v2/anime/"+str(i)+"?fields=opening_themes", headers=header)
            ed =requests.get("https://api.myanimelist.net/v2/anime/"+str(i)+"?fields=ending_themes", headers=header)
            ops.append(json.loads(op.text)['opening_themes'][0]['text'])
            eds.append(json.loads(ed.text)['ending_themes'][0]['text'])
            
        return ops, eds
        
    

            

        
        
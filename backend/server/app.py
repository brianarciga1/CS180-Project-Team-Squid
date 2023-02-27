from flask import Flask, jsonify, session,request
from flask_session import Session
from flask_cors import CORS
from getSptoken import get_sp_token
from getMALtoken import getMALtoken
from getThemes import getThemes
from addSong import addSong
import json
import os

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './.flask_session/'
Session(app)

# enable CORS
CORS(app)


@app.route('/api/sp_auth', methods=['GET'])
def sp_auth():
    if session.get("token_info",'no token') != 'no token':
        return 'auth complete'
    sp_token = get_sp_token()
    res = sp_token.get_sp_token()
    return res

@app.route('/api/mal_auth', methods=['GET'])
def mal_auth():
    if session.get("mal_token",'no token') != 'no token':
        return 'auth complete'
    mal_token = getMALtoken()
    res = mal_token.get_token()
    return res

@app.route('/api/submission', methods=['POST'])
def submission():
    themes = getThemes()
    themes.open_token()
    form = request.json
    add_song=addSong()
    add_song.open_token()
    add_song.create_list(form['playlistTitle'], form['playlistDesc'])
    add_song.add_Song(add_song.search(themes.get_themes(form)))
    return 'success'

if __name__ == '__main__':
    app.run()
from flask import Flask, jsonify, session
from flask_session import Session
from flask_cors import CORS
from getSptoken import get_sp_token
from getMALtoken import getMALtoken
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
        return session.get('token_info')
    sp_token = get_sp_token()
    res = sp_token.get_sp_token()
    return res

@app.route('/api/mal_auth', methods=['GET'])
def mal_auth():
    mal_token = getMALtoken()
    res = mal_token.get_token()
    return res

@app.route('/api/check')
def check():
    return session["token_info"]

if __name__ == '__main__':
    app.run()
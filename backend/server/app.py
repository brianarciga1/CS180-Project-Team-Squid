from flask import Flask, jsonify, session
from flask_session import Session
from flask_cors import CORS
from getSptoken import get_sp_token
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
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return None

@app.route('/sp_auth', methods=['GET'])
def sp_auth():
    sp_token = get_sp_token()
    res = sp_token.get_sp_token()
    return res

if __name__ == '__main__':
    app.run()
from flask import Flask, jsonify, session,request
from flask_session import Session
from flask_cors import CORS
from getSptoken import get_sp_token
from getMALtoken import getMALtoken
from getThemes import getThemes
from addSong import addSong
from rq import Queue
from worker import background_task
import redis
import json
import os

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)
q = Queue(connection=r)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './.flask_session/'
Session(app)

# enable CORS
CORS(app)


@app.route('/sp_auth', methods=['GET'])
def sp_auth():
    if session.get("token_info",'no token') != 'no token':
        return 'auth complete'
    sp_token = get_sp_token()
    res = sp_token.get_sp_token()
    return res

@app.route('/mal_auth', methods=['GET'])
def mal_auth():
    if session.get("mal_token",'no token') != 'no token':
        return 'auth complete'
    mal_token = getMALtoken()
    res = mal_token.get_token()
    return res

@app.route('/submission', methods=['POST'])
def submission():
    themes = getThemes()
    themes.open_token()
    add_song=addSong()
    add_song.open_token()
    form = request.json
    task = q.enqueue(background_task, form, themes, add_song)
    response = {
        "status" : "success",
        "data": {
            "task_id": task.get_id()
        }
    }
    return jsonify(response), 202

@app.route('/task/<task_id>', methods=['GET'])
def get_status(task_id):
    task = q.fetch_job(task_id)
    if task:
        response = {
            "status": "success",
            "data": {
                "task_id": task.get_id(),
                "task_status": task.get_status(),
                "task_result": task.result,
            },
        }
    else:
        response = {"status": "error"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
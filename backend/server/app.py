from flask import Flask, jsonify
from flask_cors import CORS
from scrape import UrlManager
import json

url = "https://www.crunchyroll.com/watch/GRMGQX55R/izuku-midoriya-origin"
url1 ="https://www.crunchyroll.com/watch/G4VUQZ7MX/the-new-threat"
url2 = "https://tubitv.com/tv-shows/395405/s01-e01-end-and-beginning?start=true"

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return 


if __name__ == '__main__':
    app.run()
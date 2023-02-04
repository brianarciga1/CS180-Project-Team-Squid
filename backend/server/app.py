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

url_manager = UrlManager()
url_manager.add_new_url(url1)
url_manager.add_new_url(url)
url_manager.add_new_url(url2)
resualts = []
while url_manager.has_new_url() == True:
    resualts.append(url_manager.search(url_manager.get_url()))

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return json.dumps(resualts)


if __name__ == '__main__':
    app.run()
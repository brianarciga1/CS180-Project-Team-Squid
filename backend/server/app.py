from flask import Flask, jsonify
from flask_cors import CORS
import json

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route


if __name__ == '__main__':
    app.run()
import os
from flask import Flask, request
from flask import json
from flask.json import jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    return jsonify({ "status" : "online"})

@app.route('/getWeek')
def getWeek():
    week = {}
    return jsonify(week)

if __name__ == '__main__':
    app.run(host="localhost", port=80)
    
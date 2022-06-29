import os
import json
from flask import Flask, jsonify
from pymongo import MongoClient
import requests

app = Flask(__name__)

def getDB():
    # import ipdb
    # ipdb.set_trace()

    mongoClient = MongoClient("mongodb://root-master:password-master@fz_mongodb:27017/?authMechanism=DEFAULT&authSource=db-fzsports")

    return mongoClient["db-fzsports"]

# List all teams available in the DB
app.route('/api/team')
def get_all_teams():
    response = {'message': 'List all teams available in the DB.'}
    return jsonify(response)

# List the players of the team ID
app.route('/api/teams/:<idTeam>/players', methods=['GET'])
def get_user(idTeam):
    response = {'message': 'List the players of the team ID.' + idTeam}
    return jsonify(response)

# List all players in the same position ID
app.route('/api/teams/players/:<position>', methods=['GET'])
def get_user(position):
    response = {'message': 'List all players in the same position ID.' + position}
    return jsonify(response)

@app.route('/')
def hello():
    return 'Hola FzSports!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

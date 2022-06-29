import json
from pydoc import resolve
from flask import Flask, jsonify, request, json, Response
from pymongo import MongoClient
import logging as log

app = Flask(__name__)


class MongoAPI:
    def __init__(self, data):
        log.basicConfig(level=log.DEBUG,
                        format='%(asctime)s %(levelname)s:\n%(message)s\n')
        # self.client = MongoClient("mongodb://localhost:27017/")  # When only Mongo DB is running on Docker.
        # When both Mongo and This application is running on
        self.client = MongoClient( "mongodb://root-master:password-master@fz_mongodb:27017/")
        # Docker and we are using Docker Compose

        database = data['database']
        collection = data['collection']
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data

    def read(self):
        log.info('Reading All Data')

        documents = self.collection.find({}, {'_id': False, 'plantelEquipo.equipo': True})
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        
        # pipeline = [{'$group': {'_id': {'equipo': '$carrierA'},'count': {'$sum': 1}}}]
        # return list(self.collection.aggregate(pipeline))

        # pipeline = [{"$match": 'equipo'}]
        # return self.collection.aggregate(pipeline).to_list(length=None)

        # nd_info = self.collection.index_information()
        # return nd_info
        return output[0]['plantelEquipo']['equipo']
        # return output[0]['plantelEquipo']['equipo'][0]['@nombre']



# List all teams available in the DB
@app.route('/api/team')
def get_teams():

    data = {
        "database": "db-fzsports",
        "collection": "sports"
    }

    obj1 = MongoAPI(data)
    response = obj1.read()
    return Response(response=json.dumps(response), status=200, mimetype='application/json')

    # response = {'message': 'List all teams available in the DB.'}
    # return jsonify(response)

# List the players of the team ID
@app.route('/api/teams/:<idTeam>/players', methods=['GET'])
def get_players_team(idTeam):

    data = {
        "database": "db-fzsports",
        "collection": "sports"
    }

    obj1 = MongoAPI(data)
    response = obj1.read()

    # return Response(json.dumps(response, sort_keys=True))
    # response = response[0]['@nombre']

    return Response(response=json.dumps(response), status=200, mimetype='application/json')

    # response = {'message': 'List the players of the team ID: ' + idTeam}
    # return jsonify(response)

# List all players in the same position ID
@app.route('/api/teams/players/:<position>', methods=['GET'])
def get_players_position(position):
    response = {'message': 'List all players in the same position ID.' + position}
    return jsonify(response)

@app.route('/', methods=('GET', 'POST'))
def hello():
    return 'Hola FzSports!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

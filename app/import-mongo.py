import os
import json
import xmltodict
import requests
from pymongo import MongoClient


class getScriptXML:
    def __init__(self, url, save_folder, filename):
        self.url = url
        self.save_folder = save_folder
        self.filename = filename

    def getData(self):
        if not os.path.isdir(self.save_folder):
            os.system("mkdir " + self.save_folder)

        path = self.save_folder + "/" + self.filename

        response = requests.get(self.url)
        with open(path, 'wb') as file:
            file.write(response.content)
        
        self.convertXMLtoJSON(path)

    def convertXMLtoJSON(self, path):
        with open(path, "r") as xmlfileObj:
            #Converting xml data to dictionary
            data_dict = xmltodict.parse(xmlfileObj.read())
            xmlfileObj.close()
            
            #Creating JSON object using dictionary object
            jsonObj = json.dumps(data_dict)

        if not os.path.isdir("JSON"):
            os.system("mkdir " + "JSON")

        #storing json data to json file
        with open("JSON/sports.json", "w") as jsonfileObj:
            jsonfileObj.write(jsonObj)
            jsonfileObj.close()

        self.importJSONtoMongoDB()

    def importJSONtoMongoDB(self):
        client = pymongo.MongoClient('mongodb://root-master:password-master@localhost:27017/?authMechanism=DEFAULT&authSource=db-master')
        mydb = client['db-master']
        mycol = mydb['sports']

        http_json = json.loads('JSON/sports.json')
        # use iteritems() in Python 2 instead
        for key, val in http_json.items():

            # the value must be a list for insert_many() to work
            if key == "docs" and type(val) == list:
                mycol.insert_many(val)

        # declare an empty string object
        # json_string = ''

        # use Python's open() function to load a JSON file
        # with open('JSON/sports.json', 'r', encoding='utf-8') as json_data:
            # print('JSON/sports.json TYPE:', type(json_data))

            # iterate over the _io.TextIOWrapper returned by open() using enumerate()
            # for i, line in enumerate(json_data):
                # append the parsed IO string to the JSON string
                # json_string += line
                
        # print(json_string)
        # Making Connection
        # mongoClient = MongoClient("mongodb://root-master:password-master@localhost:27017/?authMechanism=DEFAULT")

        # with open('JSON/sports.json') as f:
        #     data = json.load(f)

        

        # mycol.insert_many(data, object)
        # mycol.insert_many(json_string)

        # for y in mycol.find():
        #     print(y)

        # database
        # db = mongoClient["db-master"]

        # Created or Switched to collection
        # Collection = db["sports"]

        # Loading or Opening the json file
        # with open('JSON/sports.json') as file:
            # file_data = json.load(file)

        # print(file_data)

        # Collection.insert_many(file_data, list)
        # Collection.insert_one(file_data)

if __name__ == "__main__":
    getScriptXML(
        'https://fx-nunchee-assets.s3.amazonaws.com/data/sports.xml',
        'XML',
        'sports.xml'
    ).getData()
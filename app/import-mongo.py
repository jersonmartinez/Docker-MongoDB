import os
import requests

class getScriptXML:
    def __init__(self, url, save_folder, filename):
        self.url = url
        self.save_folder = save_folder
        self.filename = filename

    def getData(self):
        URL = self.url

        if not os.path.isdir(self.save_folder):
            os.system("mkdir " + self.save_folder)

        path = self.save_folder + "/" + self.filename

        response = requests.get(URL)
        with open(path, 'wb') as file:
            file.write(response.content)

if __name__ == "__main__":
    getScriptXML(
        'https://fx-nunchee-assets.s3.amazonaws.com/data/sports.xml',
        'XML',
        'sports.xml'
    ).getData()
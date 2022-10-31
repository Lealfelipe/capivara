import requests

from model import Item

BASE_URL = "mysql+mysqlconnector://root:1903Imortal@localhost:3306/capivara"

def capivara(database):
    for i in range(1, 2):
        response = requests.get(BASE_URL.format(i))
        content_json = response.json()
        item_json = {k: v for k, v in content_json.items() if k in dir(Item)}


        database.session.add(Item(**item_json))
        database.session.commit()


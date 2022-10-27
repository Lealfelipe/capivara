import requests

from model import Item

BASE_URL = "mysql+mysqlconnector://aluno:aluno123@localhost:3306/capivara"

def capivara_database(database):
    for i in range(1, 20):
        response = requests.get(BASE_URL.format(i))
        content_json = response.json()
        item_json = {k: v for k, v in content_json.items() if k in dir(Item)}

        database.session.add(Item(**item_json))
        database.session.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    application = Flask(__name__)
    application.config.from_object(
        "config.DevelopmentConfig")


    db.init_app(application)

    if application.config["TESTING"]:
        with application.app_context():
            db.drop_all()
            db.create_all()
            from banco.crawler import capivara_database
            capivara_database(db)

        return application

from model import *

if __name__ == "__main__":
    create_app().run(host="127.0.0.1", port=3306)
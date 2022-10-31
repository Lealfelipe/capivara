from flask import Blueprint

item_blueprint = Blueprint(
    "item_blueprint", __name__, url_prefix="/item")

from .routes import *
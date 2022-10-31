from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired

class ItemForm(FlaskForm):
    id_item = IntegerField("Identificador", validators=[DataRequired()])
    nome = StringField("Nome do Personagem", validators=[DataRequired()])
from flask import render_template
from Item import item_blueprint
from Item.forms import ItemForm
from main import db
from model import Item


@item_blueprint.route("/new", methods=["GET", "POST"])
def new_item():
    form = Itemform()

    if form.validate_on_submit():
        item = Item(id=int(form.id.data), name=str(form.name.data))
        db.session.add(item)
        db.session.commit()
        return "Personagem inserido com sucesso", 200

    return render_template("character/new.html", form=form)
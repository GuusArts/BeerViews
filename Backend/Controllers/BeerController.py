from Models.Beer import Beer
from flask import Blueprint

BeerController_blueprint = Blueprint("BeerController", __name__)

@BeerController_blueprint.route("/Brewgle/getBeerData/<id>")
def getBeerData(id):
    beer_data = __getBeer(id)
    return beer_data.get_beer_data()

def __getBeer(id):
    return Beer(id=int(id))
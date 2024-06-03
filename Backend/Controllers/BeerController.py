from Models.Beer import Beer
from flask import Blueprint

BeerController_blueprint = Blueprint("BeerController", __name__)

@BeerController_blueprint.route("/Brewgle/getBeerData/<id>")
def getBeerData(id):
    beer_data = __getBeer(id=int(id))
    return beer_data.get_beer_data()

@BeerController_blueprint.route("/Brewgle/getAllBeerNames/")
def getAllBeerNames():
    beer_data = __getBeer(id=47841)
    return beer_data.all_names()

def __getBeer(id=None):
    return Beer(id=id)
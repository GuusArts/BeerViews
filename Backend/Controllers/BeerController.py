from Models.Beer import Beer
from flask import Blueprint

BeerController_blueprint = Blueprint("BeerController", __name__)

@BeerController_blueprint.route("/Brewgle/getBeerData/<id>")
def getBeerData(id):
    beer_data = __getBeer(id=int(id))
    return beer_data.get_beer_data()

@BeerController_blueprint.route("/Brewgle/getAllBeerNames/")#TODO: Algoritmic name finder, this takes to long
def getAllBeerNamesData(loc=0):
    beers_data = []
    while True:
        try:
            beer_data = __getBeer(loc=loc)
            loc += 1
            data = beer_data.get_beer_data()
            beers_data.append(data['name'])
            print(loc)
        except:
            return beers_data

def __getBeer(id=None, loc=None):
    return Beer(id=id, loc=loc)
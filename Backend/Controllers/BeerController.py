from Models.Beer import Beer
from Models.DataLoader import DataLoader
from flask import Blueprint, jsonify

BeerController_blueprint = Blueprint("BeerController", __name__)

data_loader = DataLoader(r'D:\Documenten\Fontys\Software\Semester 6\Brewgle\Brewgle\Data\Beers.json')

@BeerController_blueprint.route("/Brewgle/getBeerData/<id>")
def getBeerData(id):
    beer = Beer.from_id(int(id), data_loader)
    return jsonify(beer.get_beer_data())

@BeerController_blueprint.route("/Brewgle/getAllBeerNames/")
def getAllBeerNames():
    names = Beer.all_names(data_loader)
    return jsonify(names)
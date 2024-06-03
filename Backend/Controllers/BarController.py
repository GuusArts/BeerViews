from Models.Bars import Bar
from Models.DataLoader import DataLoader
from flask import Blueprint, jsonify

BarController_blueprint = Blueprint("BarController", __name__)

data_loader = DataLoader(r'D:\Documenten\Fontys\Software\Semester 6\Brewgle\Brewgle\Data\Bars.json')

@BarController_blueprint.route("/Brewgle/getBarBeers/<id>")
def getBarBeers(id):
    bar = Bar.from_id(int(id), data_loader)
    return jsonify(bar.get_beers())

@BarController_blueprint.route("/Brewgle/getBarName/<id>")
def getBarName(id):
    bar = Bar.from_id(int(id), data_loader)
    return jsonify(bar.get_bar_name())

@BarController_blueprint.route("/Brewgle/getAllBars")
def getAllBars():
    bars = Bar.all_bars(data_loader)
    return jsonify([bar.get_bar() for bar in bars])

def __getBar(id):
    return Bar.from_id(int(id), data_loader)
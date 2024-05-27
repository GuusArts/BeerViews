from Models.Bars import bar
from flask import Blueprint

BarController_blueprint = Blueprint("BarController", __name__)

@BarController_blueprint.route("/Brewgle/getBarBeers/<id>")
def getBarBeers(id):
    bar_data = __getBar(id)
    return bar_data.get_beers()

@BarController_blueprint.route("/Brewgle/getBarName/<id>")
def getBarName(id):
    bar_data = __getBar(id)
    return bar_data.get_bar_name()

@BarController_blueprint.route("/Brewgle/getAllBars")
def getAllBars(id=0):
    all_bars = []
    try:
        while True:
            bar_data = __getBar(id)
            all_bars.append(bar_data.get_bar())
            id += 1
    except: 
        return all_bars
        

def __getBar(id):
    return bar(id=int(id))
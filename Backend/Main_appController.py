from Models.Bars import bar
from flask import Flask

app = Flask(__name__)

@app.route("/Brewgle/getBarData/<id>")
def getAllBars(id):
    barData = bar(id=int(id))
    return barData.get_beers()
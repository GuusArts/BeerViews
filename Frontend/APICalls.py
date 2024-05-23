import requests

LOCALHOST = "http://127.0.0.1:5000"

def getAllBeers(id):
    return requests.get(f"{LOCALHOST}/Brewgle/getBarData/{id}").json()
import requests

LOCALHOST = "http://127.0.0.1:5000"

def getAllBeers(id):
    return requests.get(f"{LOCALHOST}/Brewgle/getBarBeers/{id}").json()

def getBarName(id):
    return requests.get(f"{LOCALHOST}/Brewgle/getBarName/{id}").json()

def getAllBars():
    return requests.get(f"{LOCALHOST}/Brewgle/getAllBars").json()

def getBeerData(id):
    return requests.get(f"{LOCALHOST}/Brewgle/getBeerData/{id}").json()

def getAllBeerNames():
    return requests.get(f"{LOCALHOST}/Brewgle/getAllBeerNames").json()
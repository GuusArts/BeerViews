import requests
import json

LOCALHOST = "http://127.0.0.1:5000"

def getAllBeers(id):
    return requests.get(f"{LOCALHOST}/Brewgle/getBarBeers/{id}").json()

def getBarName(id):
    return requests.get(f"{LOCALHOST}/Brewgle/getBarName/{id}").json()

def getAllBars():
    try:
        response = requests.get("http://127.0.0.1:5000/Brewgle/getAllBars")
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except ConnectionError as e:
        print(f"Error connecting to server: {e}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def getBeerData(id):
    return requests.get(f"{LOCALHOST}/Brewgle/getBeerData/{id}").json()

def getAllBeerNames():
    return requests.get(f"{LOCALHOST}/Brewgle/getAllBeerNames").json()

def getRecommendedBeer(car, top_beers, lowest_beer, emotion):
    user = {
        "car": car,
        "top_beers": top_beers,
        "lowest_beer": lowest_beer,
        "emotion": emotion
    }
    response = requests.post(f"{LOCALHOST}/Brewgle/getRecommendedBeer", json=user)
    return response.json()
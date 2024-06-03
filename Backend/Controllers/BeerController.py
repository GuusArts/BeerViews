from Models.Beer import Beer
from Models.DataLoader import DataLoader
from flask import Blueprint, jsonify, request
import pandas as pd
import numpy as np

BeerController_blueprint = Blueprint("BeerController", __name__)

data_loader = DataLoader(r'D:\Documenten\Fontys\Software\Semester 6\Brewgle\Brewgle\Data\Beers.json')

def get_new_user_embedding(initial_ratings, beer_embeddings, beer_names):
    new_user_embedding = np.zeros(beer_embeddings.shape[1])
    count = 0
    for beer_name, rating in initial_ratings.items():
        if beer_name in beer_names:
            beer_index = beer_names.index(beer_name)
            new_user_embedding += beer_embeddings[beer_index] * rating
            count += 1
        else:
            print(f"Beer '{beer_name}' not found in the dataset. Skipping this rating.")
    if count > 0:
        new_user_embedding /= count
    else:
        print("No valid initial ratings provided. Using zero vector for new user embedding.")
    return new_user_embedding



@BeerController_blueprint.route("/Brewgle/getBeerData/<id>")
def getBeerData(id):
    beer = Beer.from_id(int(id), data_loader)
    return jsonify(beer.get_beer_data())

@BeerController_blueprint.route("/Brewgle/getAllBeerNames/")
def getAllBeerNames():
    names = Beer.all_names(data_loader)
    return jsonify(names)

@BeerController_blueprint.route("/Brewgle/getRecommendedBeer", methods=['POST'])
def getRecommendedBeer():
    user = request.get_json(force=True)  # Parse JSON data
    user_scores = {}

    for beer in user['top_beers']:
        user_scores.update({beer: 4.5})

    for beer in user['lowest_beer']:
        user_scores.update({beer: 1.0})

    beer_embeddings = pd.read_csv(r'D:\Documenten\Fontys\Software\Semester 6\Brewgle\Brewgle\Backend\Embeddings\beer_embeddings.csv')
    beer_names = Beer.all_names(data_loader)
    beer_embeddings = beer_embeddings.to_numpy()

    new_user_embedding = get_new_user_embedding(user_scores, beer_embeddings, beer_names)

    scores = np.dot(beer_embeddings, new_user_embedding)
    top_n_indices = np.argsort(scores)[-5:][::-1]
    top_n_beers = [(beer_names[i], scores[i]) for i in top_n_indices]
    return jsonify(top_n_beers)
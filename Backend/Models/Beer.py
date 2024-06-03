class Beer:
    def __init__(self, beer_data):
        self.beer = beer_data

    @classmethod
    def from_id(cls, id, data_loader):
        data = data_loader.load_data()
        for beer in data['Beers']:
            if beer['Id'] == id:
                return cls(beer)
        raise ValueError(f"Beer with ID {id} not found")

    def get_beer_data(self):
        return {
            "id": self.beer['Id'],
            "name": self.beer['Name'],
            "style": self.beer['Style'],
            "abv": self.beer['ABV'],
            "brewery": self.beer['Brewery'],
            "average score": self.beer['Average score'],
            "average score aroma": self.beer['Average score aroma'],
            "average score appearance": self.beer['Average score appearance'],
            "average score palate": self.beer['Average score palate'],
            "average score taste": self.beer['Average score taste']
        }

    @staticmethod
    def all_names(data_loader):
        data = data_loader.load_data()
        return [beer['Name'] for beer in data['Beers']]
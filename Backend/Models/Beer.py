import json
class Beer:
    def __init__(self, id):
        self.path = r'D:\Documenten\Fontys\Software\Semester 6\Brewgle\Brewgle\Data\Beers.json'
        self.json_file = self.__loadJSON()

        self.beer = None

        for beer in self.json_file['Beers']:
            if beer['Id'] == id:
                self.beer = beer
                break

        if self.beer is None:
            raise ValueError(f"Beer with ID {id} not found")
        
    def all_names(self) -> list:
        names = []

        with open(self.path, 'r') as file:
            data = json.load(file)

            for beer in data['Beers']:
                names.append(beer['Name'])
        return names

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

    def __loadJSON(self):
        with open (self.path, "r") as file:
            return json.load(file)
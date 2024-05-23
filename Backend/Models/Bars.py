import json

class bar:
    def __init__(self, id):
        self.json_file = self.__loadJSON()
        self.bar = self.json_file['Bars'][id]
        self.beers = self.bar['Beers']
        

    def get_beers(self) -> list:
        return self.beers
    

    def __loadJSON(self):
        path = r'D:\Documenten\Fontys\Software\Semester 6\Brewgle\Brewgle\Data\Bars.json'
        with open (path, "r") as file:
            return json.load(file)

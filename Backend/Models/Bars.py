import json

class bar:
    def __init__(self, id):
        self.json_file = self.__loadJSON()
        self.bar = self.json_file['Bars'][id]

        
    def get_beers(self) -> list:
        return self.bar['Beers']
    

    def get_bar_name(self) -> str:
        return self.bar['Name']
    

    def get_bar(self) -> object:
        return {
            'id': self.bar['Id'],
            'name': self.bar['Name'],
            'beer_ids': self.bar['Beer_ids']
        }


    def __loadJSON(self):
        path = r'D:\Documenten\Fontys\Software\Semester 6\Brewgle\Brewgle\Data\Bars.json'
        with open (path, "r") as file:
            return json.load(file)

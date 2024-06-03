import json

class Bar:
    def __init__(self, bar_data):
        self.bar = bar_data

    @classmethod
    def from_id(cls, id, data_loader):
        data = data_loader.load_data()
        if id < 0 or id >= len(data['Bars']):
            raise ValueError(f"Bar with ID {id} not found")
        return cls(data['Bars'][id])

    def get_beers(self) -> list:
        return self.bar['Beers']
    
    def get_bar_name(self) -> str:
        return self.bar['Name']
    
    def get_bar(self) -> dict:
        return {
            'id': self.bar['Id'],
            'name': self.bar['Name'],
            'beer_ids': self.bar['Beer_ids']
        }

    @staticmethod
    def all_bars(data_loader):
        data = data_loader.load_data()
        return [Bar(bar) for bar in data['Bars']]
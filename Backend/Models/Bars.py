import json

class bars:
    def __init__(self):
        self.path = r'..\Data\Bars.json'
        self.json_file = json.load(self.path)

    def get_all_bars(self):


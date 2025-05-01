import requests

class Scryfall_API:
    def __init__(self):
        self.placeholder = None


    def check_Valid_Card(self, card_data:dict):
        return (None == card_data['prices']['usd'])


    def get_Price(self, card_data:dict):
        return card_data['prices']['usd']


    def request_Card_Data(self, card_name: str):
        reachout = requests.get(f"https://api.scryfall.com/cards/named?fuzzy={card_name}")
        return reachout.json()
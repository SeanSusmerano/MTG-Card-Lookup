import requests

class Scryfall_API:
    def __init__(self):
        self.placeholder = None


    def check_Valid_Card(self, card_data:dict, card_foil:str):
        foil_check = False

        if(len(card_foil) > 0):
            foil_check = True

        if('status' in card_data):
            return False
        elif((None == card_data['prices']['usd']) and (not foil_check)):
            return False
        elif((None == card_data['prices']['usd_foil']) and foil_check):
            return False
        else:
            return True
    #Add a way to differentiate what the issue is, missing price, or card couldn't be found.


    def get_Price(self, card_data:dict, card_foil: str):

        if(len(card_foil) > 0):
            return card_data['prices']['usd_foil']
        else:
            return card_data['prices']['usd']


    def request_Card_Data(self, card_name: str):
        reachout = requests.get(f"https://api.scryfall.com/cards/named?fuzzy={card_name}")
        return reachout.json()
import requests
import time


class Card_Searcher:
    def __init__(self):
        self.removeDocument = None
        self.keepDocument = None
        self.searchAgainDocument = None

        self.searchList = []
    


    def check_If_Bigger_Than_Dollar(self, dictionary_Object: dict):
        try:
            price = float(dictionary_Object['prices']['usd'])
            return ( (price > 1.0), False )
        except:
            self.write_To_Search_Again(dictionary_Object, 0)
            return (False, True)


    def check_If_None(self, dictionary_Object: dict):
        return dictionary_Object['prices']['usd'] == 'None'


    def data_Request(self, search: str): 
        cleaned_Search = search.replace('\n','')
        reachout = requests.get(f"https://api.scryfall.com/cards/named?fuzzy={cleaned_Search}")
        return reachout.json()


    def open_Documents(self, status: bool):
        if(status):
            self.removeDocument = open('CardsToRemove.txt','a')
            self.keepDocument = open('CardsToKeep.txt','a')
            self.searchAgainDocument = open('CardsToResearch.txt','a')
        else:
            self.removeDocument.close()
            self.keepDocument.close()
            self.searchAgainDocument.close()


    def overwrite_Search_List(self):
        document_to_rewrite = open('CardsToSearch.txt','w')
        new_text = ''.join(self.searchList)
        document_to_rewrite.write(new_text)
        document_to_rewrite.close()


    def populate_Search_List(self):
        #English Characters only please. Breaks if there are non-english characters.

        document_to_Search = open('CardsToSearch.txt','r')
        self.searchList = document_to_Search.readlines()
        document_to_Search.close()


    def remove_From_Search_List(self):
        del self.searchList[0]


    def write_To_Document(self, dictionary_Object: dict, keep_Card: bool):
        if(keep_Card):
            text = f"{dictionary_Object['name']}: {dictionary_Object['prices']['usd']}\n"
            self.keepDocument.write(text)
        else:
            text = f"{dictionary_Object['name']}\n"
            self.removeDocument.write(text)


    def write_To_Search_Again(self, dictionary_Object: dict, error = None):
        #error = 0: No Price
        #error = 1: Card could not be found

        if(error == None):
            print(dictionary_Object)
        elif(error == 0):
            text = f"Card has no price: {dictionary_Object['name']}\n"
            self.searchAgainDocument.write(text)
        elif(error == 1):
            self.searchAgainDocument.write(f"{dictionary_Object['details']}\n")

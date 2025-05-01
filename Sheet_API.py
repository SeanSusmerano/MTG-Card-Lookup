import gspread
from google.oauth2.service_account import Credentials
from datetime import date

class Google_API:
    def __init__(self, id = None, link = None):
        self.credentials_filename = "credentials.json"
        self.document_id = id
        self.document_link = link

        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        creds = Credentials.from_service_account_file(self.credentials_filename, scopes = scopes)
        client = gspread.authorize(creds)

        if(self.document_id == None and self.document_link == None):
            raise FileNotFoundError
        elif(self.document_id == None):
            self.document = client.open_by_url(self.document_link)
        elif(self.document_link == None):
            self.document = client.open_by_key(self.document_id)

        self.already_searched_position = -1
        self.unable_to_search_position = -1
        self.sell_individually_position = -1

        self.Already_Searched_Worksheet = self.document.worksheet("Already_Searched")
        self.Do_Not_Search_Worksheet = self.document.worksheet("Do_Not_Search")
        self.Unable_To_Search_Worksheet = self.document.worksheet("Unable_To_Search")
        self.Search_List_Worksheet = self.document.worksheet("Search_List")
        self.Sell_Individually_Worksheet = self.document.worksheet("Sell_Individually")

        self.date = date.today()


    def Add_Already_Searched(self,card_name:str):
        if(self.already_searched_position == -1):
            card_List = self.Already_Searched_Worksheet.col_values(1)
            self.already_searched_position = len(card_List)
        self.already_searched_position += 1

        self.Already_Searched_Worksheet.update_acell(f"A{self.already_searched_position}", card_name)
        self.Already_Searched_Worksheet.update_acell(f"B{self.already_searched_position}", self.date)


    def Add_Unable_To_Search(self, card_name:str, reason:str):
        if(self.unable_to_search_position == -1):
            card_List = self.Unable_To_Search_Worksheet.col_values(1)
            self.unable_to_search_position == len(card_List)
        self.unable_to_search_position += 1

        self.Unable_To_Search_Worksheet.update_acell(f"A{self.unable_to_search_position}", card_name)
        self.Unable_To_Search_Worksheet.update_acell(f"B{self.unable_to_search_position}", reason)


    def add_Sell_Individually(self, card_name:str, price:str):
        if(self.sell_individually_position == -1):
            card_List = self.Sell_Individually_Worksheet.col_values(1)
            self.sell_individually_position = len(card_List)
        sell_individually_position += 1
        
        self.Sell_Individually_Worksheet.update_acell(f"A{self.sell_individually_position}", card_name)
        self.Sell_Individually_Worksheet.update_acell(f"B{self.sell_individually_position}", price)
        self.Sell_Individually_Worksheet.update_acell(f"C{self.sell_individually_position}", self.date)


    def clear_Search_List(self):
        card_List = self.Search_List_Worksheet.col_values(1)
        self.Search_List_Worksheet.batch_clear([f"A2:A{len(card_List)}"])


    def grab_Already_Searched_List(self):
        card_Name_List = self.Already_Searched_Worksheet.col_values(1)
        search_Date_List = self.Already_Searched_Worksheet.col_values(2)
        return dict(zip(card_Name_List[1:],search_Date_List[1:]))
    

    def grab_Do_Not_Search_List(self):
        card_List = self.Do_Not_Search_Worksheet.col_values(1)
        return card_List[1:]


    def grab_Search_List(self):
        search_List = self.Search_List_Worksheet.col_values(1)
        return search_List [1:]
    

    def grab_Sell_Individually_List(self):
        sell_List = self.Sell_Individually_Worksheet.col_values(1)
        return sell_List[1:]
    

    def update_Already_Searched_Card(self, card_name:str):
        card_List = self.Already_Searched_Worksheet.col_values(1)
        if(card_name in card_List):
            card_Index = card_List.index(card_name)

            self.Already_Searched_Worksheet.update_acell(f"B{card_Index}", self.date)
            return True
        else:
            return False
        

    def update_Sell_Individually(self, card_name:str, price:str):
        card_List = self.Sell_Individually_Worksheet.col_values(1)
        if(card_name in card_List):
            card_Index = card_List.index(card_name)

            self.Sell_Individually_Worksheet.update_acell(f"B{card_Index}", price)
            self.Sell_Individually_Worksheet.update_acell(f"C{card_Index}", self.date)
            return True
        else:
            return False
        
    
    def set_Filename(self, filename: str):
        self.credentials_filename = filename


    def set_Sheet_ID(self, ID: str):
        self.sheet_id = ID



def main():
    bb = Google_API(id = "private")
    print(bb.add_Sell_Individually("test"))

if (__name__ == "__main__"):
    main()
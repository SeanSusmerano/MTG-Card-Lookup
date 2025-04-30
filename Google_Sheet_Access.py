import gspread
from google.oauth2.service_account import Credentials
from datetime import date

class Google_API:
    def __init__(self):
        self.credentials_filename = "credentials.json"
        self.document_id = None
        self.document_link = None

        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        creds = Credentials.from_service_account_file(self.credentials_filename, scopes = scopes)
        client = gspread.authorize(creds)

        self.document = client.open_by_key(self.document_id)

        self.already_searched_position = -1
        self.unable_to_search_position = -1
        self.sell_individually_position = -1


        self.date = date.today()


    def Add_Already_Searched(self,card_name:str):
        worksheet = self.document.worksheet("Already_Searched")
        if(self.already_searched_position == -1):
            card_List = worksheet.col_values(1)
            self.already_searched_position = len(card_List)
        self.already_searched_position += 1

        worksheet.update_acell(f"A{self.already_searched_position}", card_name)
        worksheet.update_acell(f"B{self.already_searched_position}", self.date)


    def Add_Unable_To_Search(self, card_name:str):
        worksheet = self.document.worksheet("Unable_To_Search")
        if(self.unable_to_search_position == -1):
            card_List = worksheet.col_values(1)
            self.unable_to_search_position == len(card_List)
        self.unable_to_search_position += 1

        worksheet.update_acell(f"A{self.unable_to_search_position}", card_name)


    def add_Sell_Individually(self, card_name:str, price:str):
        worksheet = self.document.worksheet("Sell_Individually")
        if(self.sell_individually_position == -1):
            card_List = worksheet.col_values(1)
            self.sell_individually_position = len(card_List)
        sell_individually_position += 1
        
        worksheet.update_acell(f"A{self.sell_individually_position}", card_name)
        worksheet.update_acell(f"B{self.sell_individually_position}", price)
        worksheet.update_acell(f"C{self.sell_individually_position}", self.date)
        return


    def grab_Already_Searched_List(self):
        worksheet = self.document.worksheet("Already_Searched")
        card_Name_List = worksheet.col_values(1)
        search_Date_List = worksheet.col_values(2)
        return dict(zip(card_Name_List[1:],search_Date_List[1:]))


    def grab_Search_List(self):
        worksheet = self.document.worksheet("Search_List")
        search_List = worksheet.col_values(1)
        return search_List [1:]
    
    
    def set_Filename(self, filename: str):
        self.credentials_filename = filename


    def set_Sheet_ID(self, ID: str):
        self.sheet_id = ID

def main():
    bb = Google_API()
    print(bb.add_Sell_Individually("test"))

if (__name__ == "__main__"):
    main()
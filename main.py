import Sheet_API, Scry_API
from datetime import date, datetime

def check_If_Worth_Searching(card_name: str, already_searched:dict):
    days_since_searched = -1

    if(card_name in already_searched):
        days_since_searched = (date.today() - datetime.strptime(already_searched[card_name], '%Y-%m-%d').date()).days

    if(days_since_searched > 1):
        return True
    else:
        return False


def main():

    proper_link = False

    while(not proper_link):
        user_input = input("What is the link to the Google Sheets Document(Or type 'exit' to stop this script):")

        if("docs.google.com/spreadsheets/" in user_input):
            proper_link = True
        elif("exit" in user_input.lower()):
            return
        else:
            print("I'm sorry that doesn't appear to be a proper input.")
    
    document = Sheet_API.Google_API(link = user_input)
    search_List = document.grab_Search_List()
    do_Not_Search_List = document.grab_Do_Not_Search_List()
    already_Searched_Dictionary = document.grab_Already_Searched_List()
    scry = Scry_API.Scryfall_API()

    for each_card in search_List:
        should_Check = check_If_Worth_Searching(each_card, already_Searched_Dictionary)
        if((each_card in do_Not_Search_List) or (each_card == "")):
            continue

        card_data = scry.request_Card_Data(each_card)
        valid_card = scry.check_Valid_Card(card_data)
        
        if(valid_card and should_Check):
            card_price = scry.get_Price(card_data)
            document.update_Already_Searched_Card(each_card)
        elif(valid_card and (each_card not in already_Searched_Dictionary)):
            card_price = scry.get_Price(card_data)
            document.Add_Already_Searched(each_card)
        else:
            continue

        if(float(card_price)>1.0):
            document.add_Sell_Individually(each_card,card_price)
        



if(__name__ == "__main__"):
    main()
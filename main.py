import Sheet_API, Scry_API, time
from datetime import date, datetime

def check_If_Worth_Searching(card_name: str, card_foil: str, already_searched:dict):
    days_since_searched = -1

    if(len(card_foil) > 0):
        card_name += " (f)"

    if(card_name in already_searched):
        days_since_searched = (date.today() - datetime.strptime(already_searched[card_name], '%Y-%m-%d').date()).days

    if(days_since_searched > 1):
        return True
    else:
        return False


def wait():
    print("Quick minute break to not exceed Google write Request Limit.")
    time.sleep(60)


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
    search_Dict = document.grab_Search_List()
    do_Not_Search_List = document.grab_Do_Not_Search_List()
    already_Searched_Dictionary = document.grab_Already_Searched_List()
    scry = Scry_API.Scryfall_API()
    search_Length = len(search_Dict)
    counter = 0

    for each_card in search_Dict:
        counter += 1
        if(document.write_count > 55):
            wait()
            document.write_count = 0

        should_Check = check_If_Worth_Searching(each_card, search_Dict[each_card], already_Searched_Dictionary)
        if((each_card in do_Not_Search_List) or (each_card == "")):
            print(f"Completed: {counter}/{search_Length}")
            continue

        card_data = scry.request_Card_Data(each_card)
        valid_card = scry.check_Valid_Card(card_data, search_Dict[each_card])
        card_price = 0
        
        if(valid_card and should_Check):
            card_price = scry.get_Price(card_data, search_Dict[each_card])
            document.update_Already_Searched_Card(each_card, search_Dict[each_card])
        elif(valid_card and (each_card not in already_Searched_Dictionary)):
            card_price = scry.get_Price(card_data, search_Dict[each_card])
            document.Add_Already_Searched(each_card, search_Dict[each_card])
        elif(not valid_card):
            document.Add_Unable_To_Search(each_card, search_Dict[each_card], "Unable to find card Data.")
        else:
            document.Add_Unable_To_Search(each_card, search_Dict[each_card], "Unable to determine issue.")

        if(float(card_price)>1.0):
            document.add_Sell_Individually(each_card, search_Dict[each_card], card_price)
        print(f"Completed: {counter}/{search_Length}")
    
    #Clear search list
    document.Search_List_Worksheet.batch_clear(["A2:A1000"])

if(__name__ == "__main__"):
    main()
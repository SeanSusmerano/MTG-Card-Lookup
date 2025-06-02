import Sheet_API, Scry_API, time
from datetime import date, datetime

def check_If_Worth_Searching(card_name: str, foil_Bool: bool, already_searched:dict):
    days_since_searched = -1

    if(foil_Bool):
        card_name += " (f)"

    print(card_name)

    if(card_name in already_searched):
        days_since_searched = (date.today() - datetime.strptime(already_searched[card_name], '%Y-%m-%d').date()).days

    if(days_since_searched > 1):
        return True
    else:
        return False


def check_If_Foil(foil_List:list, card_Index: int):
    try:
        index_Value = foil_List[card_Index]
    except:
        return False
    
    if(len(index_Value) > 0):
        return True
    else:
        return False


def check_If_Proper_Link(): #Continue working on this.
    proper_link = False

    while(not proper_link):
        user_input = input("What is the link to the Google Sheets Document(Or type 'exit' to stop this script):")

        if("docs.google.com/spreadsheets/" in user_input):
            proper_link = True
        elif("exit" in user_input.lower()):
            return
        else:
            print("I'm sorry that doesn't appear to be a proper input.")


def get_Card_Index(card_List: list, card_Name: str):
    #[Card_List, Index_Int, Duplicate_Bool]
    duplicate_Count = card_List.count(card_Name)
    first_Occurance = -1

    if(duplicate_Count > 1):
        first_Occurance = card_List.index(card_Name)

        #Update the card list and remove the first occurance with "placeholder-abc-123"
        card_List[first_Occurance] = "placeholder-abc-123"

        return [card_List, first_Occurance, True]
    elif(duplicate_Count == 1):
        first_Occurance = card_List.index(card_Name)
        return [card_List, first_Occurance, False]
    else:
        return [card_List, first_Occurance, False]


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
    search_List_Data = document.grab_Search_List()
    do_Not_Search_List = document.grab_Do_Not_Search_List()
    already_Searched_Dictionary = document.grab_Already_Searched_List()
    scry = Scry_API.Scryfall_API()
    search_Length = len(search_List_Data[0][1:])
    counter = 0

    for each_card in search_List_Data[0][1:]:
        counter += 1
        if(document.write_count > 55):
            wait()
            document.write_count = 0

        card_List_Check = get_Card_Index(search_List_Data[0],each_card)

        if(card_List_Check[2]):
            search_List_Data[0] = card_List_Check[0]
            card_Index = card_List_Check[1]

        elif((not card_List_Check[2]) and (card_List_Check[1] == -1)):
            print("Something went wrong with this card")
            print(f"Completed: {counter}/{search_Length}")
            continue
        else:
            card_Index = card_List_Check[1]

        foil_Bool = check_If_Foil(search_List_Data[1], card_Index)

        should_Check = check_If_Worth_Searching(each_card, foil_Bool, already_Searched_Dictionary)
        if((each_card in do_Not_Search_List) or (each_card == "")):
            print(f"Completed: {counter}/{search_Length}")
            continue

        card_data = scry.request_Card_Data(each_card)
        valid_card = scry.check_Valid_Card(card_data, foil_Bool)
        card_price = 0
        if(foil_Bool):
            new_card_name = each_card + " (f)"
        else:
            new_card_name = each_card
        
        if(valid_card and should_Check):
            card_price = scry.get_Price(card_data, foil_Bool)
            document.update_Already_Searched_Card(each_card, foil_Bool)
        elif(valid_card and (new_card_name not in already_Searched_Dictionary)):
            card_price = scry.get_Price(card_data, foil_Bool)
            document.Add_Already_Searched(each_card, foil_Bool)
        elif(not valid_card):
            document.Add_Unable_To_Search(each_card, foil_Bool, "Unable to find card Data.")
        else:
            document.Add_Unable_To_Search(each_card, foil_Bool, "Unable to determine issue.")

        if(float(card_price)>1.0):
            document.add_Sell_Individually(each_card, foil_Bool, card_price)
        print(f"Completed: {counter}/{search_Length}")
    
    #Clear search list
    document.Search_List_Worksheet.batch_clear(["A2:A1000"])
    document.Search_List_Worksheet.batch_clear(["B2:B1000"])

if(__name__ == "__main__"):
    main()
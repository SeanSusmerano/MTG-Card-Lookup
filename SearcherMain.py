import Card_Searcher

def main(counter = 0, search_amount = 0, list_to_search = []):
    searcher = Card_Searcher.Card_Searcher()

    searcher.open_Documents(True)

    if(list_to_search == []):
        searcher.populate_Search_List()
    else:
        searcher.searchList = list_to_search

    if(search_amount == 0):
        search_amount = len(searcher.searchList)

    max_Count_Per_Session = counter + 100

    while(counter < search_amount):
        if(counter == max_Count_Per_Session):
            break

        each_entry = searcher.searchList[counter]

        data = searcher.data_Request(each_entry)

        if('details' in list(data.keys())):
            #Could not find card
            searcher.write_To_Search_Again(data, 1)

            counter += 1
            print(f'Completed: {counter}/{search_amount}')

            continue
        keep = searcher.check_If_Bigger_Than_Dollar(data)
        if(keep[1]):
            counter += 1
            print(f'Completed: {counter}/{search_amount}')
            continue
        else:
            searcher.write_To_Document(data, keep[0])

        counter += 1
        print(f'Completed: {counter}/{search_amount}')

    searcher.open_Documents(False)

    if(search_amount > counter):
        main(counter, search_amount,searcher.searchList)
    else:
        return

if(__name__ == "__main__"):
    main()
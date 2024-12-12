
import json

def view_all_books(all_info):
    with open("all_info.json", "r") as fp:
        all_info = json.load(fp)

    if all_info != []:
        for book in all_info:
            for key,value in book.items():
                print(f"{key}: {value}")
            print('\n')
    else:
        print("No Book found.")
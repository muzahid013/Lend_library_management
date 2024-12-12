# def save_all_books(all_info):
#     with open("all_info.csv", "w") as fp:
#         for book in all_info:
#             line = f"{book['title']}, {book['author']}, {book['isbn']}, {book['year']}, {book['price']}, {book['quantity']}\n"
#             fp.write(line)

import json

def save_all_books(all_info):
    with open("all_info.json", "w") as fp:
        json.dump(all_info, fp, indent=4)
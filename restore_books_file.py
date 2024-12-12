import json

def restore_all_books(all_info):
    with open("all_info.json", "r") as fp:
        all_info = json.load(fp)
    return all_info

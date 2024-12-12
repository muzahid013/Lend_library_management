import save_all_books

def delete_books(all_info):
    search_book = input("Enter Book Title to Return: ")
    if all_info != []:
        for book in all_info:
            if book["book_title"] == search_book:
                all_info.remove(book)
                save_all_books.save_all_books(all_info)
                print("Borrower information removed successfully.")
                return all_info
    else:
        print("Borrower information not found.")

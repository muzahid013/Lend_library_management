import add_borrowers_file, view_all_books, restore_books_file, delete_book_file, save_all_books


all_info = []
print("Welcome to Lend Book System")
# global books_count
books_count = int(input('How many book the library has: '))

while True:
    print("0. Exit")
    print("1. Add borrower's information: ")
    print("2. View All Borrower informations: ")
    print("3. Borrower Want To Return Book. ")
    print("4. No. of available books:  ")

    save_all_books.save_all_books(all_info)
    all_info = restore_books_file.restore_all_books(all_info)

    menu = input("Select any number: ")
    
    if menu == "0":
        print("Thanks for using Lend Book Management System ")
        break
    elif menu == "1":
        if books_count > 0:
            all_info = add_borrowers_file.add_borrower(all_info)
            books_count = books_count - 1
        else:
            print(f"There are not enough books available to lend")
    elif menu == "2":
        view_all_books.view_all_books(all_info)
    elif menu == "3":
        delete_book_file.delete_books(all_info)
        books_count = books_count + 1
    elif menu == "4":
        print(f'No. of available books: {books_count}')
    else:
        print("Choose a valid number")
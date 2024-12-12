from save_all_books import save_all_books
import datetime

def add_borrower(all_info):
    book_booking_date = datetime.datetime.now()
    return_due_date = book_booking_date + datetime.timedelta(days=7)

    while True:
        try:
            print('\nFirst letter must be letter.')
            book_title = input("Enter Book Title: ")
            borrower_name = input("Enter Borrower Name: ")
            if book_title[:1].isalpha() and borrower_name[:1].isalpha():
                break
        except:
            print("book title and borrower name should start with latter.")

    while True:
        try:
            phone_number = int(input("Enter 11 digit phone number: "))
            if len(str(phone_number)) == 10:
                break
        except:
            print("Invalid input. Please enter a phone number.")



    book = {
        "book_title":               book_title,
        "borrower_name":            borrower_name,
        "phone_number":             f'0{phone_number}',
        "book_booking_date":        book_booking_date.strftime("%d-%m-%Y"),
        "return_due_date":          return_due_date.strftime("%d-%m-%Y"),
    }
    
    all_info.append(book)
    save_all_books(all_info)

    print("Information Added Successully")
    
    return all_info
    
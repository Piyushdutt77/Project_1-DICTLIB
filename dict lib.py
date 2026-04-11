import datetime

library_books = {}

def add_books():
    name = input("Enter the book name: ").strip().lower()
    if name in library_books:
        print("Book already exists")
    else:
        library_books[name] = {"status": "Available", "issued_on": None}
        print("Book added successfully")

def show_books():
    if not library_books:
        print("No books available")
    else:
        print("\nLibrary Books:")
        for book, details in library_books.items():
            status = details["status"]
            if status == "Issued":
                issued_on = details["issued_on"]
                days_issued = (datetime.date.today() - issued_on).days
                print(f"{book.title()} : {status} (Issued {days_issued} days ago)")
            else:
                print(f"{book.title()} : {status}")

def issue_books():
    name = input("Enter the book name: ").strip().lower()
    if name in library_books:
        if library_books[name]["status"] == "Available":
            library_books[name]["status"] = "Issued"
            library_books[name]["issued_on"] = datetime.date.today()
            print("Book issued successfully")
        else:
            print("Book is already issued")
    else:
        print("Book not found")

def return_books():
    name = input("Enter the book name: ").strip().lower()
    if name in library_books:
        if library_books[name]["status"] == "Issued":
            issued_on = library_books[name]["issued_on"]
            days_issued = (datetime.date.today() - issued_on).days
            allowed_days = 7
            fine_per_day = 50
            fine = 0
            if days_issued > allowed_days:
                fine = (days_issued - allowed_days) * fine_per_day
            library_books[name]["status"] = "Available"
            library_books[name]["issued_on"] = None
            print(f"Book returned successfully. It was issued for {days_issued} days.")
            if fine > 0:
                print(f"Fine applicable: ₹{fine}")
        else:
            print("Book was not issued")
    else:
        print("Book not found")

def library():
    while True:
        print("\nLibrary Menu ")
        print("1. Add Books")
        print("2. Show Books")
        print("3. Issue Books")
        print("4. Return Books")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_books()
        elif choice == 2:
            show_books()
        elif choice == 3:
            issue_books()
        elif choice == 4:
            return_books()
        elif choice == 5:
            print("Thank You!")
            break
        else:
            print("Invalid choice")

library()

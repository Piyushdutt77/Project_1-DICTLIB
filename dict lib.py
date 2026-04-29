books = {}
issued_books = {}

def add_books():
    name = input("Enter book name: ")
    if name in books:
        print("Book already exists")
    else:
        books[name] = "available"
        print("Book added")

def show_books():
    if books == {}:
        print("No books available")
    else:
        print("Books:")
        for i in books:
            print(i, "=", books[i])

def issue_books():
    name = input("Enter book name: ")
    if name in books:
        if books[name] == "available":
            student = input("Enter student name: ")
            days = int(input("For how many days: "))
            if days > 0:
                books[name] = "issued"
                issued_books[name] = [student, days]
                print("Book issued")
            else:
                print("Invalid days")
        else:
            print("Book already issued")
    else:
        print("Book not found")

def calculate_fine(extra):
    fine = 0
    for i in range(1, extra + 1):
        fine = fine + (10 * i)
    return fine

def return_books():
    name = input("Enter book name: ")
    if name in issued_books:
        used = int(input("Enter days used: "))
        allowed = issued_books[name][1]
        if used > allowed:
            extra = used - allowed
            fine = calculate_fine(extra)
            print("Late return")
            print("Fine:", fine)
        else:
            print("Returned on time")
        books[name] = "available"
        issued_books.pop(name)
        print("Book returned")
    else:
        print("Book not issued")

def library():
    while True:
        print("1 Add book")
        print("2 Show books")
        print("3 Issue book")
        print("4 Return book")
        print("5 Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_books()
        elif choice == "2":
            show_books()
        elif choice == "3":
            issue_books()
        elif choice == "4":
            return_books()
        elif choice == "5":
            print("Exit")
            break
        else:
            print("Wrong choice")
library()

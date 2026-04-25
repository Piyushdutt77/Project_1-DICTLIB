import datetime

library_books = {}
issued_books = {}

def today():
    return datetime.date.today()

def calculate_fine(issue_date, allowed_days):
    days_used = (today() - issue_date).days

    if days_used <= allowed_days:
        return days_used, 0

    extra_days = days_used - allowed_days
    fine = 0

    for i in range(1, extra_days + 1):
        week = (i // 7) + 1
        fine = fine + (10 * week)

    return days_used, fine

def add_books():
    name = input("Enter book name: ")

    name = name.strip().lower()

    if name in library_books:
        print("Book already exists")
    else:
        library_books[name] = {"status": "Available"}
        print("Book added")

def show_books():
    if library_books == {}:
        print("No books")
        return

    print("Books in library:")

    for book in library_books:
        if book in issued_books:
            issue_date = issued_books[book]["issue_date"]
            days = (today() - issue_date).days
            print(book.title(), "- Issued for", days, "days")
        else:
            print(book.title(), "- Available")

def issue_books():
    name = input("Enter book name: ")
    name = name.strip().lower()

    if name not in library_books:
        print("Book not found")
        return

    if name in issued_books:
        print("Already issued")
        return

    student = input("Enter student name: ")
    days = int(input("Enter days: "))

    issued_books[name] = {
        "student": student,
        "issue_date": today(),
        "days": days
    }

    print("Book issued")

def return_books():
    name = input("Enter book name: ")
    name = name.strip().lower()

    if name not in issued_books:
        print("Not issued")
        return

    record = issued_books[name]

    days_used, fine = calculate_fine(record["issue_date"], record["days"])

    del issued_books[name]

    print("Returned")
    print("Student:", record["student"])
    print("Days:", days_used)

    if fine > 0:
        print("Fine:", fine)
    else:
        print("No fine")

def library():
    while True:
        print("Library Menu")
        print("1 Add Books")
        print("2 Show Books")
        print("3 Issue Book")
        print("4 Return Book")
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
            print("Thank you.")
            break
        else:
            print("Wrong choice")

library()

library_books = {}

def add_books():
    name = input("Enter the book name: ").strip().lower()
    if name in library_books:
        print("Book already exists")
    else:
        library_books.update({name: "Available"})
        print("Book added successfully")

def show_books():
    if not library_books:
        print("No books available")
    else:
        print("\nLibrary Books:")
        for book, status in library_books.items():
            print(f"{book.title()} : {status}")

def issue_books():
    name = input("Enter the book name: ").strip().lower()
    if name in library_books:
        if library_books[name] == "Available":
            library_books.update({name: "Issued"})
            print("Book issued successfully")
        else:
            print("Book is already issued")
    else:
        print("Book not found")

def return_books():
    name = input("Enter the book name: ").strip().lower()
    if name in library_books:
        if library_books[name] == "Issued":
            library_books.update({name: "Available"})
            print("Book returned successfully")
        else:
            print("Book was not issued")
    else:
        print("Book not found")

def library():
    while True:
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

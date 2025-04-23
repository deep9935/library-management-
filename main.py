
def login():
    print("=== Library Login ===")
    username = input("Username: ")
    password = input("Password: ")
    
    with open("users.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(",")
            if username == stored_username and password == stored_password:
                print("Login successful!\n")
                return True
    print("Invalid username or password.\n")
    return False

def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    with open("books.txt", "a") as file:
        file.write(f"{book_id},{title},{author},Available\n")
    print("Book added successfully.")

def view_books():
    print("\n=== Book List ===")
    with open("books.txt", "r") as file:
        for line in file:
            book_id, title, author, status = line.strip().split(",")
            print(f"ID: {book_id}, Title: {title}, Author: {author}, Status: {status}")
    print()

def search_book():
    search = input("Enter title or author to search: ").lower()
    found = False
    with open("books.txt", "r") as file:
        for line in file:
            book_id, title, author, status = line.strip().split(",")
            if search in title.lower() or search in author.lower():
                print(f"ID: {book_id}, Title: {title}, Author: {author}, Status: {status}")
                found = True
    if not found:
        print("Book not found.")

def issue_book():
    book_id = input("Enter book ID to issue: ")
    books = []
    issued = False
    with open("books.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == book_id and data[3] == "Available":
                data[3] = "Issued"
                issued = True
            books.append(",".join(data))
    
    with open("books.txt", "w") as file:
        for book in books:
            file.write(book + "\n")
    
    if issued:
        print("Book issued successfully.")
    else:
        print("Book not found or already issued.")

def return_book():
    book_id = input("Enter book ID to return: ")
    books = []
    returned = False
    with open("books.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == book_id and data[3] == "Issued":
                data[3] = "Available"
                returned = True
            books.append(",".join(data))
    
    with open("books.txt", "w") as file:
        for book in books:
            file.write(book + "\n")
    
    if returned:
        print("Book returned successfully.")
    else:
        print("Book not found or already available.")

def main_menu():
    while True:
        print("\n1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    if login():
        main_menu()

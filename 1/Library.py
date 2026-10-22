
# Practical 2: Library Inventory System using Classes and Objects


class Book:
    def __init__(self, title, author, quantity):
        self.title = title
        self.author = author
        self.quantity = quantity

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Quantity:", self.quantity)
        print("-" * 30)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")
        return book

    def display_books(self):
        if len(self.books) == 0:
            print("Library is empty.")
        else:
            print("\n--- Library Inventory ---")
            for book in self.books:
                book.display()

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print("\nBook found:")
                book.display()
                return book

        print("Book not found.")
        return None


def main():
    library = Library()

    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Search Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")

            try:
                quantity = int(input("Enter quantity: "))

                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                else:
                    book = Book(title, author, quantity)
                    library.add_book(book)

            except ValueError:
                print("Please enter a valid number for quantity.")

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            title = input("Enter the title to search: ")
            library.search_book(title)

        elif choice == "4":
            print("Exiting Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

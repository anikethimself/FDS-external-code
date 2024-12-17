"""
Write a Python program for department library which has N books, write functions for following: 
a) Delete the duplicate entries 
b) Display books in ascending order based on cost of books 
c) Count number of books with cost more than 500. 
d) Copy books in a new list which has cost less than 500. 
"""

class Book:
    def __init__(self, title, author, cost):
        self.title = title
        self.author = author
        self.cost = cost

    def __repr__(self):
        return f"{self.title} by {self.author} - Rs.{self.cost:.2f}"

def delete_duplicates(books):
    unique_books = {book.title: book for book in books}
    return list(unique_books.values())

def display_books_sorted(books):
    sorted_books = sorted(books, key=lambda book: book.cost)
    for book in sorted_books:
        print(book)

def count_books_above_cost(books, threshold=500):
    return sum(1 for book in books if book.cost > threshold)

def copy_books_below_cost(books, threshold=500):
    return [book for book in books if book.cost < threshold]

if __name__ == "__main__":
    library_books = [
        Book("Python Programming", "John Doe", 450),
        Book("Data Structures", "Jane Smith", 600),
        Book("Machine Learning", "Alice Johnson", 700),
        Book("Python Programming", "John Doe", 450), 
        Book("Introduction to Algorithms", "Robert Brown", 400),
        Book("Deep Learning", "Alice Johnson", 650)
    ]
    
    print("List of all books (also book name with duplicates):")
    for book in library_books:
        print(book)

    library_books = delete_duplicates(library_books)
    print("\nBooks after deleting duplicates:")
    for book in library_books:
        print(book)

    print("\nBooks sorted by cost:")
    display_books_sorted(library_books)

    count_above_500 = count_books_above_cost(library_books)
    print(f"\nNumber of books with cost more than 500: {count_above_500}")

    cheap_books = copy_books_below_cost(library_books)
    print("\nBooks with cost less than 500:")
    for book in cheap_books:
        print(book)


class Book:
    
    def __init__(self, book, author, num_pages):
        self.book = book
        self.author = author
        self.num_pages = num_pages
        
    def __str__(self):
        return f"'{self.book}' by {self.author}"
    
    def __eq__(self, other):
        return self.book == self.book and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self, keyword):
        return keyword in self.book or keyword in self.author
    
    def __getitem__(self, key):
        if key == "book":
            return self.book
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"
    
    
        
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 193)
book2 = Book("1984", "George Orwell", 328)
book3 = Book("Pride and Prejudice", "Jane Austen", 347) 
book4 = Book("Pride and Prejudice", "Jane Austen", 398) 

# print(book3)

# print(book3 == book4)

# print(book3 < book4)

# print(book3 > book4)

# print(book3 + book4)

# print("Great" in book1)

print(book1['num_pagses'])
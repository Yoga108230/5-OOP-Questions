#Composition Over Inheritance: Create a Book class with a Author class included within it, demonstrating composition over inheritance.

class Author:
    def __init__(self, name, nationality):
        self.name= name
        self.nationality= nationality
    def get_information(self):
        return f"Author: {self.name}, Nationality: {self.nationality}"
    
class Book:
    def __init__(self, title, author, year):
        self.title= title
        self.author= author
        self.year= year
    def get_details(self):
        return f"{self.title}, ({self.year}) by {self.author.get_information()}"
    
author= Author("Vincent Barayoga", "Filipino")

book= Book("2020", author, 2025)

print(book.get_details())
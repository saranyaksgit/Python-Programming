class Publisher:
    def __init__(self, publisher_id, publisher_name):
        self.publisher_id = publisher_id
        self.publisher_name = publisher_name
    
    def show_details(self):
        print("Publisher ID:", self.publisher_id)
        print("Publisher Name:", self.publisher_name)

class Book(Publisher):
    def __init__(self, publisher_id, publisher_name, title, author):
        super().__init__(publisher_id, publisher_name)
        self.title = title
        self.author = author
    
    def show_details(self):
        super().show_details()
        print("Title:", self.title)
        print("Author:", self.author)

class Python(Book):
    def __init__(self, publisher_id, publisher_name, title, author, price, no_of_pages):
        super().__init__(publisher_id, publisher_name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages
    
    def show_details(self):
        super().show_details()
        print("Price:", self.price)
        print("No. of Pages:", self.no_of_pages)

python_book = Python(123, "ABC Publications", "Learning Python", "John Doe", 500, 300)
python_book.show_details()


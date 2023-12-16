class Book():

    def __init__(self, title, author, page) -> None:
        self.title = title
        self.author = author
        self.page = page
    
    def __repr__(self) -> str:
        return f"Book title : {self.title}\nBook author : {self.author}"
    
    def __len__(self):
        return self.page
    

my_book = Book("Python Introduction","Suraj Yadav", 300)

print(my_book)
print(len(my_book))
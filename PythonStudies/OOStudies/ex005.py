class Book:
    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn=isbn
        self.title=title
        self.author=author
        self.publisher=publisher
        self.pages=pages
        self.price=price
        self.copies=copies


    def display(self):
        print(f"""isbn: {self.isbn}
title: {self.title}
price: US${self.price}
copies: {self.copies}
in stock? {self.in_stock()}""")

    def in_stock(self):
        if self.copies>0:
            return True
        else:
            return False



book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,0)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)

book1.display()
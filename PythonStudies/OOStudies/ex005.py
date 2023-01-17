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
        print(f"""-=-=-=-=-=BOOK-=-=-=-=-=
isbn: {self.isbn}
title: {self.title}
price: US${self.price}
copies: {self.copies}
in stock? {self.in_stock()}
-=-=-=-=-=-=-=-=-=-=-=-=""")

    def in_stock(self):
        if self.copies>0:
            return True
        else:
            return False

    def sell(self, qtd=1):
        if self.in_stock():
            self.copies-=qtd
        else:
            print(f'Book out of order')

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, val):
        if 50<=val<=1000:
            self._price=val
        else:
            raise ValueError('Price cannot be more than 1000 and less than 50')


book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)

book1.sell()
book1.display()

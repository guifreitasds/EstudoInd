class SalesPerson:
    names = []
    total_revenue=0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sales_amount = 0
        SalesPerson.names.append(self.name)

    def make_sale(self, money):
        self.sales_amount += money
        SalesPerson.total_revenue+=money

    def show(self):
        print(self.name, self.age, self.sales_amount)

    @classmethod
    def showClass(cls):
        print(F"""=-=-=-FUNCIONÁRIOS=-=-=-=
{cls.names}
TOTAL DE VENDAS: R${cls.total_revenue}
-=-=-=-=-=-=-=-=-=-=-=-=-""")


s1 = SalesPerson('Bob', 25)
s2 = SalesPerson('Ted', 22)
s3 = SalesPerson('Jack', 27)

s1.make_sale(1000)
s1.make_sale(1200)
s2.make_sale(5000)
s3.make_sale(3000)
s3.make_sale(8000)

s1.show()
s2.show()
s3.show()

SalesPerson.showClass()
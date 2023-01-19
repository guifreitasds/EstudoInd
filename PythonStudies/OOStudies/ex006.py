class Fraction:
    def __init__(self, nr, dr=1):
        if nr<0 and dr<0:
            self.nr = nr * -1
            self.dr = dr * -1
        elif nr>0 and dr<0:
            self.nr = nr * -1
            self.dr = dr * -1
        else:
            self.nr = nr
            self.dr = dr

    def show(self):
        return f'{self.nr}/{self.dr}'


    def add(self,f2):
        if type(f2)==int:
            f2 = Fraction(f2)
        numer = (self.nr*f2.dr)+(self.dr*f2.nr)
        denom = self.dr*f2.dr
        f4 = Fraction(numer, denom)
        print(f'Fraction solved: {f4.show()}')
        return f4


    def multiply(self, f2):
        if type(f2)==int:
            f2 = Fraction(f2)
        numer = self.nr*f2.nr
        denom = self.dr*f2.dr
        f = Fraction(numer,denom)
        print(f'Fraction solved: {f.show()}')
        return f

x = int(input('Type a numerator: '))
y = int(input('Type a denominator: '))
z = int(input('Type a numerator: '))
a = int(input('Type a denominator: '))



f1 = Fraction(2,3)
print(f1.show())
f2 = Fraction(3,4)
print(f2.show())
f3 = f1.multiply(f2)
print(f3.show())
f3 = f1.add(f2)
print(f3.show())
f3 = f1.add(5)
print(f3.show())
f3 = f1.multiply(5)
print(f3.show())
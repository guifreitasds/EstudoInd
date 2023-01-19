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

    def display(self):
        return f'{self.nr}/{self.dr}'


    def add(self,f2):
        if type(f2)==int:
            f2 = Fraction(f2)
        numer = (self.nr*f2.dr)+(self.dr*f2.nr)
        denom = self.dr*f2.dr
        f4 = Fraction(numer, denom)
        print(f'Fraction solved: {f4.display()}')
        return f4


    def multiply(self, f2):
        if type(f2)==int:
            f2 = Fraction(f2)
        numer = self.nr*f2.nr
        denom = self.dr*f2.dr
        f = Fraction(numer,denom)
        print(f'Fraction solved: {f.display()}')
        return f

x = int(input('Type a numerator: '))
y = int(input('Type a denominator: '))
z = int(input('Type a numerator: '))
a = int(input('Type a denominator: '))

f1 = Fraction(x,y)
f2 = Fraction(z, a)
print(f1.display())
f1.multiply(5)
f1.add(f2)
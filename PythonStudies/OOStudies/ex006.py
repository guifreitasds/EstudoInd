class Fraction:
    def __init__(self, nr, dr):
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
        print(f'{self.nr}/{self.dr}')
    
    def multiply(self, nr1, dr1, nr2, dr2=1):
        numer = nr1*nr2
        denom = dr1*dr2
        f3=Fraction(numer,denom)
        print(f'Fraction solved: {f3.display()}')
        return f3

x = int(input('Type a numerator: '))
y = int(input('Type a denominator: '))
z = int(input('Type a numerator: '))
a = int(input('Type a denominator: '))

f1 = Fraction(x,y)
f2 = Fraction(z, a)
f1.display()
f1.multiply(f1.nr,f1.dr, f2.nr, f2.dr)
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
        return f'{self.nr}/{self.dr}'

    def add(self, nr1, dr1, nr2, dr2=1):
        numer = (nr1*dr2+nr2*dr1)
        denom = dr1*dr2
        f4 = Fraction(numer, denom)
        print(f'Fraction solved: {f4.display()}')
        return f4

    def addanotherform(self, f1,f2):
        numer = (f1.nr*f2.dr)+(f1.dr*f2.nr)
        denom = f1.dr*f2.dr
        f4 = Fraction(numer, denom)
        print(f'Fraction solved: {f4.display()}')
        return f4
    
    def multiply(self, nr1, dr1, nr2, dr2=1):
        numer = nr1*nr2
        denom = dr1*dr2
        f = Fraction(numer,denom)
        print(f'Fraction solved: {f.display()}')
        return f

    def multiplyanotherform(self, f1, f2):
        numer = f1.nr*f2.nr
        denom = f1.dr*f2.dr
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
f1.multiplyanotherform(f1,f2)
f1.add(f1.nr,f1.dr, f2.nr,f2.dr)
f1.addanotherform(f1,f2)
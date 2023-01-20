class Fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:
            self.nr *= -1
            self.dr *= -1

    def show(self):
        return f'{self.nr}/{self.dr} and reduced = {self.nr/Fraction.hcf(self.nr,self.dr):.0f}/{self.dr/Fraction.hcf(self.nr,self.dr):.0f}'


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

    @staticmethod
    def hcf(x, y):
        x = abs(x)
        y = abs(y)
        smaller = y if x > y else x
        s = smaller
        while s > 0:
            if x % s == 0 and y % s == 0:
                break
            s -= 1
        return s



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
print(f1.hcf(2,3))
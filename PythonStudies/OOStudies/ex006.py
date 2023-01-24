class Fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:
            self.nr *= -1
            self.dr *= -1

    def show(self):
        return f'{self.nr}/{self.dr} and reduced = {self.nr/Fraction.hcf(self.nr,self.dr):.0f}/{self.dr/Fraction.hcf(self.nr,self.dr):.0f}'


    def __add__(self,f2):
        if type(f2)==int:
            f2 = Fraction(f2)
        numer = (self.nr*f2.dr)+(self.dr*f2.nr)
        denom = self.dr*f2.dr
        f4 = Fraction(numer, denom)
        print(f'Fraction solved: {f4.show()}')
        return f4

    def __sub__(self,f2):
        if type(f2)==int:
            f2 = Fraction(f2)
        numer = (self.nr*f2.dr)-(self.dr*f2.nr)
        denom = self.dr*f2.dr
        f4 = Fraction(numer, denom)
        print(f'Fraction solved: {f4.show()}')
        return f4


    def __mul__(self, f2):
        if type(f2)==int:
            f2 = Fraction(f2)
        numer = self.nr*f2.nr
        denom = self.dr*f2.dr
        f = Fraction(numer,denom)
        print(f'Fraction solved: {f.show()}')
        return f

    def __eq__(self, other):
        return (self.nr*other.dr)==(self.dr*other.nr)
    def __ne__(self, other):
        return (self.nr*other.dr)!=(self.dr*other.nr)
    def __lt__(self, other):
        return (self.nr * other.dr) < (self.dr * other.nr)
    def __le__(self, other):
        return (self.nr * other.dr) <= (self.dr * other.nr)

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
f2 = Fraction(2,3)
f3 = f1+f2
f3.show()


f3 = f1*f2
f3.show()

print(f1==f2, f1!=f2)
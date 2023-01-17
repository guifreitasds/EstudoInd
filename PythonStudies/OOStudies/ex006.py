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

x = int(input('Type a numerator: '))
y = int(input('Type a denominator: '))

f1 = Fraction(x,y)
f1.display()
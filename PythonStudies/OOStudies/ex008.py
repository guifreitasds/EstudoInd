class Circle:
    def __init__(self, radius):
        self._radius=radius
        self.diameter=2*radius
        self.circunference=radius*3.14*2

    def area(self):
        return 3.14*self.radius*self.radius

    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, value):
        if(self._radius>0):
            self._radius=value
        else:
            raise ValueError(F'Valor {value} não é aceito, tente um valor positivo!')


c1=Circle(3)

print(f'{c1.area():.2f}')
print(c1.circunference)
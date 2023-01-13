class Person:
    def set_details(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f'O nome dessa pessoa é {self.name}')
        print(f'A idade dessa pessoa é {self.age} anos')

    def greet(self):
        print('Hello, how are you doing?')


p1=Person()


p1.set_details("Jorge", 25)
p1.get_details()


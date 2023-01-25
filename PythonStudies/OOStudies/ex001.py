class Person:
    def set_details(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f'The name of this person is {self.name}')
        print(f'{self.name} is {self.age} years old')

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False

    def greet(self):
        print(f'Hello, i am {self.name}, how are you doing?')


p1=Person()


p1.set_details("Jorge", 25)
p1.get_details()


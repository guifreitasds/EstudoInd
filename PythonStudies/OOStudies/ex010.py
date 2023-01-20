class Employee:
    allowed_domains = {'yahoo.com', 'gmail.com', 'outlook.com'}
    def __init__(self, name, email):
        self.name = name
        self._email = email

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, new):
        domain = new[new.index('@') + 1:]
        if domain in Employee.allowed_domains:
            self._email = new
        else:
            raise RuntimeError()


    def display(self):
        print(self.name, self.email)


e1 = Employee('John', 'john@gmail.com')
e2 = Employee('Jack', 'jack@yahoo.com')
e3 = Employee('Jill', 'jill@outlook.com')
e4 = Employee('Ted', 'ted@yahoo.com')
e5 = Employee('Tim', 'tim@gmail.com')
e6 = Employee('Mike', 'mike@yahoo.com')


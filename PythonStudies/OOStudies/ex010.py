class Employee:
    domains=set()
    allowed_domains = {'yahoo.com', 'gmail.com', 'outlook.com'}
    def __init__(self, name, email):
        self.name = name
        if email[email.index('@')+1:] in Employee.allowed_domains:
            self.email = email
        else:
            raise RuntimeError()
        Employee.domains.add(self.email[self.email.index('@'):])


    def display(self):
        print(self.name, self.email)


e1 = Employee('John', 'john@gmail.com')
e2 = Employee('Jack', 'jack@yahoo.com')
e3 = Employee('Jill', 'jill@outlook.com')
e4 = Employee('Ted', 'ted@yahoo.com')
e5 = Employee('Tim', 'tim@gmail.com')
e6 = Employee('Mike', 'mike@yahoo.com')



print(Employee.domains)

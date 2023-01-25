from ex001 import *

class Student(Person):
    def greet(self):
        print(f"Hello, i am a Student")

class Teacher(Person):
    def greet(self):
        print(f"Hello, i am a Teacher")

class TeachingAssistant(Teacher, Student):
    def greet(self):
        print(f'Hello, i am a Teaching Assistant')

t1=TeachingAssistant("Jorge", 18)
t1.greet()
t1.get_details()
class Course:
    def __init__(self, title, instructor, price, lectures):
        self.title=title
        self.instructor=instructor
        self.price=price
        self.lectures=lectures
        self.users=[]
        self.ratings=0
        self.avg_rating=0

    def __str__(self):
        return f"""{self.title} Course
Instructor: {self.instructor}
Rating: {self.avg_rating}
Price: US${self.price}
"""

    def new_user(self, new):
        self.users.append(new)

    def receive_rating(self, val):
        self.avg_rating=(self.avg_rating*self.ratings+val)/(self.ratings+1)
        self.ratings+=1

    def show_details(self):
        print(f"""{self.lectures} Lectures
{self.users.length()} Users 
""")

class VideoCourse(Course):
    def __init__(self, title, instructor, price, lectures,leng):
        super().__init__(title, instructor, price, lectures)
        self.length_video=leng


class PdfCourse(Course):
    def __init__(self, title, instructor, price, lectures, pages):
        super().__init__(title, instructor, price, lectures)
        self.pages=pages

c1 = Course('PHP', 'Guilherme', 10, 20)

c1.receive_rating(9)
c1.receive_rating(10)
c1.receive_rating(5)
c1.receive_rating(7)
print(c1)



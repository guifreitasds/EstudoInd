class Course:
    def __init__(self, title, instructor, price, lectures, users, ratings, avg_rating):
        self.title=title
        self.instructor=instructor
        self.price=price
        self.lectures=lectures
        self.users=users
        self.ratings=ratings
        self.avg_rating=avg_rating

    def __str__(self):
        print(f"""{self.title}
Instructor: {self.instructor}
Rating: {self.avg_rating}
Price: US${self.price}
""")

    def new_user(self, new):
        self.users.append(new)

    def receive_rating(self, val):
        self.ratings.append(val)

    def show_details(self):
        print(f"""{self.lectures} Lectures
{self.users.length()} Users 
""")

class VideoCourse(Course):
    def __init__(self, title, instructor, price, lectures, users, ratings, avg_rating, leng):
        super().__init__(title, instructor, price, lectures, users, ratings, avg_rating)
        self.length_video=leng


class PdfCourse(Course):
    def __init__(self, title, instructor, price, lectures, users, ratings, avg_rating, pages):
        super().__init__(title, instructor, price, lectures, users, ratings, avg_rating)
        self.pages=pages



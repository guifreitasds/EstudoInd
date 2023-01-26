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
""")

    d

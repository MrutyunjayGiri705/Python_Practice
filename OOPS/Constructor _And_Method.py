class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("My name is", self.name)

s1 = Student("Mrutyunjay")
s1.show()
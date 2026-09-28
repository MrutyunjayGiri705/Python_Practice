class Student:
    college = "NIT"

    @classmethod
    def show_college(cls):
        print(cls.college)

Student.show_college()
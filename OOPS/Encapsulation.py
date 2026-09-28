# class Student:
#     def __init__(self):
#         self.name = "Mrutyunjay"

# s1 = Student()

# print(s1.name)
# class Student:
#     def __init__(self):
#         self._name = "Mrutyunjay"

# s1 = Student()

# print(s1._name)
class Student:
    def __init__(self):
        self.__name = "Mrutyunjay"

    def show(self):
        print(self.__name)

s1 = Student()
s1.show()
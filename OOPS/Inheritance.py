class Parent:
    def show_parent(self):
        print("I am Parent")

class Child(Parent):
    def show_child(self):
        print("I am Child")

c = Child()

c.show_parent()
c.show_child()
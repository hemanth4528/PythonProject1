class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return self.marks > 40


s1 = Student("Alice", 55)
s2 = Student("Bob", 35)

if s1.is_passed():
    print(f"{s1.name} has passed.")
else:
    print(f"{s1.name} has failed.")

if s2.is_passed():
    print(f"{s2.name} has passed.")
else:
    print(f"{s2.name} has failed.")

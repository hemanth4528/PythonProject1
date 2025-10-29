class Employee:
    company_name = "TechCorp"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name


emp1 = Employee("Alice")
emp2 = Employee("Bob")

print(f"{emp1.name} works at {emp1.company_name}")
print(f"{emp2.name} works at {emp2.company_name}")

Employee.change_company("CV CORP ")

print(f"{emp1.name} works at {emp1.company_name}")
print(f"{emp2.name} works at {emp2.company_name}")

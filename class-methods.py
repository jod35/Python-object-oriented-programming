from datetime import date

class Employee:
    def __init__(self,name,age):
        self.age=age
        self.name=name


    def displayInfo(self):
        return f"Name {self.name} age {self.age}"

    @classmethod
    def fromBirthYear(cls,name,birth_year):
        return cls(name=name,age=(date.today().year-birth_year))


emp1=Employee(name="Jonathan",age=23)
emp2=Employee.fromBirthYear(name="Jerry",birth_year=1985)


print(emp1.displayInfo())
print(emp2.displayInfo())





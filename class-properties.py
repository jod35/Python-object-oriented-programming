#creating properties for classes
class Employee:
    id=None
    email=None
    first_name=None
    last_name=None
    salary=None

emp1=Employee()

emp1.id=1
emp1.email="jonathan@company.com"

emp1.specialization=None

print(emp1.id)
print(emp1.email)
print(emp1.specialization)


emp2=Employee()
emp2.nationality="Ugandan"

print(emp2.nationality)
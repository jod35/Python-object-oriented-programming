#the initializer function
class Employee:
    def __init__(self,id,age,email
    ,first_name,last_name):
        self.id=id
        self.age=age
        self.email=email
        self.first_name=first_name
        self.last_name=last_name

        print("Object Created")


emp1=Employee(id=1,age=22,email="jonathan@company.com",
    first_name="Jonathan",
    last_name="Bacon"
)

emp2=Employee(id=1,age=22,
    email="jane@company.com",
    first_name="Jane",
    last_name="Doe"
)

print(emp1.email)
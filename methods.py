#the initializer function
class Employee:
    def __init__(self,id,age,email,first_name,last_name):
        self.id=id
        self.age=age
        self.email=email
        self.first_name=first_name
        self.last_name=last_name

        print("Object Created")



    def getEmail(self):
        return self.email


    def getAge(self):
        return self.age


emp1=Employee(id=1,age=22,
    email="jonathan@company.com",
    first_name="Jonathan",
    last_name="Bacon"
)

emp2=Employee(
    id=2,age=23,
    first_name="Jane",
    last_name="Doe",
    email="janedoe@company.com"
)


print(emp1.getEmail())
print(emp2.getEmail())
print(emp1.getAge())
print(emp2.getAge())
class Employee:
    def __init__(self,id, name,email,salary):
        self.id=id
        self.name=name
        self.__email=email
        self.__salary=salary



    #public method
    def __displaySalary(self):
        print(f"Salary {self.__salary}")


new_employee=Employee(id=1,name="Steven",email="steven@company.com",salary=200000)

print(new_employee._Employee__salary)

new_employee._Employee__displaySalary()


class Employee:

    def __init__(self,id,name,email,password):
        self.__id=id
        self.__name=name
        self.__email=email
        self.__password=password

    def getName(self):
        return self.__name

    def setName(self,name):
        self.__name=name

    def login(self,email,password):
        if (email==self.__email) and (password == self.__password):
            print("Access Granted")

        else:
            print("Access Denied")

new_employee=Employee(id=1,name="Jonathan",email="jonathan@company.com",
    password="password"
)

new_employee.login("jonathan@company.com","password")

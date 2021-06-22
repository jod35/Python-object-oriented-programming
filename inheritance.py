# Employee -> Teacher

class Employee:
    def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age

    def getAge(self):
        return self.age


class Teacher(Employee):
    def __init__(self,name,email,age,class_room):
        self.class_room=class_room

        super().__init__(name,email,age)

    def displayInfo(self):
        print(f"Teacher <name:{self.name} email ={self.email} age={new_teacher.getAge()} class ={self.class_room}")


new_teacher=Teacher(name="Joe",email="joe@company.com",
                        age=35,class_room="class 5"
    )

print(new_teacher.getAge())
print(new_teacher.displayInfo())


#super function
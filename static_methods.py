class Employee:

    age=23
    name="Jonathan"

    @staticmethod
    def bmi(height,weight):
        return (weight/(height**2))




print(Employee.bmi(10,23))


# Author: Prakash
# This type of inheritance is MultiLevel inheritance.


class Person():  # First Class which Doesn't inherit any class
    country = "India"

    def breath(self):
        print("Person Breathing....")


class Employee(Person):  # Second Class which inherit from Person class
    company = "Jaguar"

    def getInfo(self):
        print("Jaguar is a TATA Company.")

    def breath(self):  # when we call breath from instance of Employee class, this will overwrite the method from Person class.
        print("i am an employee and i am Breathing in style....")


class Programmer(Employee):  # Third Class which inherit from Employee class which in returns inherit from Person class
    # This class have access to both Person class attribute and Employee class Attribute
    company = "AUDI"

    def getInfo(self):  # when we call getInfo from instance of Programmer class this will overwrite the method from Employee class.
        print("We are Bathing in Dollars.")

    def breath(self):  # when we call breath from instance of Programmer class this will overwrite the method from Employee class.
        print("i am Programmer and i don't know why i am Breathing....")


p = Person()
p.breath()
# print(p.company) #This will throw Error

e = Employee()
e.breath()
print(e.company)

pr = Programmer()  # Programmer inherit from Employee class
pr.breath()
print(pr.company)
print(pr.country)

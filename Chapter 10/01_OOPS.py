# Author: Prakash

# Sample OOPS code to sumofno no

'''
This is an Example of a class, classes are blueprint for creating an object of class, class don't take memory by themselves 
they take memory when we instantiate an obj of a class, classes can contain variable and function/method 
variable in class are refered as "data members/Attribute/field" of that class.
function/method in class are refered as "Member functions/method/behavior" of that class.
'''


class Number:
    def sum(self):
        return self.a + self.b


'''
An object is simply a collection of data (variables) and methods (functions) that act on those data. 
Similarly, a class is a blueprint for that object.
'''
num = Number()  # Here we are creating a obj of class Number Which is named as num(Instantiating an obj).
# An object has two characteristics:
# attributes
# behavior

num.a = 12  # data member(variable), of obj named num. is attribute
num.b = 45  # data member(variable), of obj named num. is attribute

s = num.sum()  # we are calling member function/method of class Number using obj num and storing it in s(behavior)
print(s)

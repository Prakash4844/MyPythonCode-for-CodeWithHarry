# Practice set Q1
# Author: Prakash


def maximum(num1, num2, num3):
    if (num1 > num2):
        if (num1 > num3):
            return num1
        else:
            return num3
    else:
        if (num2 > num3):
            return num2
        else:
            return num3


m = maximum(45, 94, 32)

print("The maximum value is " + str(m))

print(f"The maximum value is {m}")

# Practice set Q5
# Author: Prakash

sumofno = 0

no = int(input("Enter a no. to find sumofno of natural no. till it: "))  # Getting a no. from user and casting to int

for i in range(1, no + 1):
    sumofno += i

print(f"Sum of first {no} natural numbers is: {sumofno}")

# Practice set Q4
# Author: Prakash

no = int(input("Enter a no. to find if it's prime or not: "))  # Getting a no. from user and casting to int
if no > 1:  # Checking if no. is greater than 1
    for i in range(2, no):  # Looping from 2 to no. - 1
        if no % i == 0:  # Checking if no. is divisible by any no. from 2 to no. - 1
            print("Not a prime no.")  # Printing if no. is divisible by any no. from 2 to no. - 1
            break  # Breaking the loop
    else:  # Executing if no. is not divisible by any no. from 2 to no. - 1
        print("Prime no.")  # Printing if no. is not divisible by any no. from 2 to no. - 1
else:  # Executing if no. is less than or equal to 1
    print("Not a prime no.")  # Printing if no. is less than or equal to 1

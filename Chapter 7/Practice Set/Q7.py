# Practice set Q7
# Author: Prakash

n = 3

for i in range(3):
    print(" " * (n - i - 1), end="")
    print("*" * (2 * i + 1), end="")
    print(" " * (n - i - 1))

'''
The end parameter in the print function is used to add any string. At the end of the output of the print statement in python.

By default, the print function ends with a newline.

Passing the whitespace to the end parameter (end=‘ ‘) indicates that the end character has to be identified by whitespace and not a newline.
'''
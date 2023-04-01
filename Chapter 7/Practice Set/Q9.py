# Practice set Q9
# Author: Prakash

# hollow square pattern

n = 3
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

'''
The end parameter in the print function is used to add any string. At the end of the output of the print statement in python.

By default, the print function ends with a newline.

Passing the whitespace to the end parameter (end=‘ ‘) indicates that the end character has to be identified by whitespace and not a newline.
'''
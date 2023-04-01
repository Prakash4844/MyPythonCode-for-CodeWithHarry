# Python program to Open and Read lines from file using readline() function
# Author: Prakash

f = open("Chapter 9/02_readline/sample.txt")

data = f.readline()  # readline can be used to read only the first line from a file having multiple line of content
print(data)
data = f.readline()  # if readline is used again then next line(2nd Line) will be read
print(data)
data = f.readline()  # if readline is used again then next line(3rd Line) will be read
print(data)

f.close()

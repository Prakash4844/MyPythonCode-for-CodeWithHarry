# Python program to Open and write into file
# Author: Prakash

# opening Empty file in write mode

# FOR USER TO DO : (Check if it is empty if not, then delete it's content)

f = open("Chapter 9/03_Writing_in_files/sample1.txt", 'w')
# if file wasn't already there then it will be created

# f.write("Whatever")

f.write(" Whatever, Previous line is, it will be overwritten by this line")  # write function will overwrite the whole file

# for appending we can open the file in append mode

f.close()

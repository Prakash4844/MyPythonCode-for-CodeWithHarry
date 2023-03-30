# Solution of Practice Set Q4
# Date: Nov 23, 2021
# Author: Prakash

import os

# Printing contents of Custom Directory (Parent Dir.)
li = os.listdir("../")
print(li)

# Printing constents of Working Directory
print(os.listdir())

'''Info
Syntax: os.listdir(path)

Parameters:
path (optional) : path of the directory

Return Type: This method returns the list of all files and directories in the specified path. The return type of this method is list.
'''

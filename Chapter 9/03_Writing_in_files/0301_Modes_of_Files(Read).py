'''
Python file modes
Don’t confuse, read about every mode as below.

r = for reading – The file pointer is placed at the beginning of the file. This is the default mode.

r+ = Opens a file for both reading and writing. The file pointer will be at the beginning of the file.

w = Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, 
    creates a new file for writing.
    
w+ = Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, 
    it creates a new file for reading and writing.
    
rb = Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file.

rb+ = Opens a file for both reading and writing in binary format.

wb+ = Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. 
    If the file does not exist, it creates a new file for reading and writing.
    
a = Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, 
    the file is in the append mode. If the file does not exist, it creates a new file for writing.
    
ab = Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. 
    That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
    
a+ = Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. 
    The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
    
ab+ = Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. 
    The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
    
x = open for exclusive creation, failing if the file already exists (Python 3)
'''

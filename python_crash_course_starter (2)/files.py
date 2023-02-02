# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile_mr = open('myfile.txt', 'w') #in here it write the myfile.txt 

# Get some info
print('Name: ', myFile_mr.name)
print('Is Closed : ', myFile_mr.closed)
print('Opening Mode: ', myFile_mr.mode)

# Write to file
myFile_mr.write('I love Python')
myFile_mr.write(' and JavaScript')
myFile_mr.close()

# Append to file
myFile_mr = open('myfile.txt', 'a')
myFile_mr.write(' I also like PHP')
myFile_mr.close()

# Read from file
myFile_mr = open('myfile.txt', 'r+')
text_mr = myFile_mr.read(100)
print(text_mr)
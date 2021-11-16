# This program opens, create, read, and close text files on a Windows OS
# print message 
print("Welcome to Python file handler for Windows OS")

# open file located in current directory
f = open("demofile.txt")

# read the whole file
print(f.read())

# read single line
#print(f.readline())

# close the file
f.close()

# create a new file, x-returns an error if already exist, w-overwrite context, a- append context
f2 = open("myfile.txt", "w")
f2.write("new text file contents go here")
f2.close()

f2 = open("myfile.txt")
print(f2.read())
f2.close()

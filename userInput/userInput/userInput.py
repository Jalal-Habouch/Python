
# this program is used to demonstrate keyboard input in Python

# read user input from keyboard, and output to command line 
in1 = input("Enter text here: ")
print("You have entered "+in1)

# read user input, convert to integer, then concatenate it with output string
in2 = input("Enter a number so I get you its double: ")
answer = int(in2)
print("My answer is: "+str(answer*2))

# read multiple user inputs, store as array, then output 
in3 =input("How many items you want me to memorize? ")
counter1 = int(in3)
i=0
items3=[]
while i<counter1: 
    items3.append(input("Enter new item: "))
    i=i+1

print("I remember ... ")
print(items3)
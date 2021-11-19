# This program is demonstrate search alogrithms in Python based on on line article
# https://stackabuse.com/search-algorithms-in-python/
# https://www.w3schools.com/python/module_random.asp

import random

# generate 100 random intgers between 1 and 100
list=[]
for x in range(99): 
   list.append(random.randrange(1,100,1))
print(list)

# use 'in' operater to find if a number exists in the list
in1 = int(input("Type a number to see if it exists in the list: "))
print("result :"+ str(in1 in list))

# use ' not in' operater to find if a number does not exist in the list
in2 = int(input("Type a number to see if it does NOT exist in the list: "))
print("result :"+ str(in2 not in list))


# linear search
def linearSearch(listSource, keyword):
    for i in range(len(listSource)):
        if listSource[i] == keyword:
            return i
    return -1

in3=int(input("Enter a number to find it using linear search algorithm: "))
print("The number is located at position: "+str(linearSearch(list, in3)))

# binary search
def binarySearch(listSource, keyword):
    first=0
    last=len(listSource)-1
    index=-1
    while (first<=last) and (index==-1):
        mid=(first+last)//2
        if listSource[mid]==keyword:
            index=mid
        else:
            if keyword < listSource[mid]:
                last=mid-1
            else:
                first=mid+1
    return index

list2= list.copy()
list2.sort()
print("Sorting the list in ascending order...")
print(list2)
in4=int(input("Enter a number to find it using Binary search algorithm: "))
print("The number is located at position: "+str(binarySearch(list2, in4)))



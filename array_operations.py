from array import *

arr = array('i',[])

n = int(input("Enter the length of the array"))

for i in range(n):
    x = int(input("Enter the value"))
    arr.append(x)
print (arr)

value = int(input("Enter the value to search"))
for i in arr:
    if i==value:
        print("Element found",+value)
        break
    print("Element not found")



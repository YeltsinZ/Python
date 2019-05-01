pos = -1
def search (list,n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i += 1  
    return False
list = [5,6,4,7,8,12,9]
print("Enter the element you wanna search :")
n = int(input())

if search(list,n):
    print("Element Found")
else:
    print("Element not Found")
pos = -1

def search(list,n):
    l = 0
    u = len(list)-1

    while l <=u:
        mid = (l + u) //2 #// will give integer division
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid
            else:
                u = mid
list = [4,7,8,12,45,99,102,702,10987,99945]
n = 12

if search(list,n):
    print("Element found at Index:",pos+1)
else:
    print("Element not found")
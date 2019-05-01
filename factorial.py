def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
    return f

print("Enter the number to find the factorial")
x = int(input())
result = fact(x)
print(result)
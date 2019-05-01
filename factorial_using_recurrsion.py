
def fact(n):
    if n == 0:
        return 1
    n = n * fact(n-1)
    return n
print("Enter the number to find its factorial : ")
x = int(input())
result = fact(x)
print(result)


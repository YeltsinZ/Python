def fib():
    a = 0
    b = 1
    print(a, b)
    print("Enter the range")
    n = int(input())
    c = 0
    while (c < n):
        print(c)
        c = a + b
        a = b
        b = c
fib()






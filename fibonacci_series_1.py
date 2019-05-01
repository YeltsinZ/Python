def fib(n):
    a = 0
    b = 1
    if n < 0:
        print("Invalid range for fibonacci")
    else:
        if n == 1:
            print(a)
        else:
            print(a)
            print(b)
            for i in range(2, n):
                c = a + b
                print(c)
                a = b
                b = c
print("Enter the range of fibonacci series to be printed")
x = int(input())
fib(x)

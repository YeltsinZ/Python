square = lambda a : a * a
side = lambda  a : 4*a
print("Enter the number to perform calculations")
x = int(input())
result1 = square(x)
result2 = side(x)
print("Square of the number :", result1)
print("Area of the square:", result2)

#Addition of 2 numbers
add = lambda a,b:a+b
print("This is addition of two numbers")
print("Enter the first number:")
i = int(input())
print("Enter the second number:")
j = int(input())
result3 = add(i,j)
print("Result",result3)
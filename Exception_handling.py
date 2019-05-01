#Exception handling in Python
print("Lets do the division of two numbers")
print("Enter the 1st number: ")
a = int(input())
print("Enter the 2nd number: ")
b = int(input())
try:
    print("Resource Open") # This can be a database connection.
    c = a / b
    print("Result: ", c)
except Exception:
    print("Hey.!! You cannot divide a number by zero")

finally:
    print("Resource Closed") # If this is a database connection it will be closed.

print("Bye..!!!")

### To print the exception message
try:
    c = a / b
except Exception as e:
    print("This is the error message : ", e)
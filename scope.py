'''
Python Scope follows the LEGB Rule:

Local
Enclosing Function locals
Global
Built-in

Built-in(Python) - Naming preassigned in the buil-in names module:
open, range, SyntaxError,...
'''

x = 25

def myfunc():
    x = 50 # This is a local variable.
    return x

#print(x)
#print(myfunc())
myfunc()
print(x)

#Enclosing function locals
name = 'This is a gloabl name'

def greet():
    name = "Sammy"

    def hello():
        print(("hello" + name))

greet()


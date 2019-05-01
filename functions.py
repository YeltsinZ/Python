
def greet():
    print("Hello")
    print("welcome to python")

greet()

def add(x,y):
    result = x +y
    print(result)

add(5,10)

def update(x):
    x = 10
    print(id(x))
    print(x)

a= 20
print(id(a))
update(a)
print("a = ",a)


#variable length arguments
def sum(a,*b):
    print(a)
    print(b)
sum(2,3,4,7,8)

#keyworded  variable length Arguments in python
#**kwargs

def person(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)
person('yeltsin',age=28,address='Bangalore',mob = 9047462613)


#passing a list to a function


for i in range(len(list)):
    print("Enter the value")
    list += i


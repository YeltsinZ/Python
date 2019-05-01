from _functools import *
def is_even(n):
    return n % 2 == 0

numbers = [1,2,3,4,5,6,7,8,9,10]
#FITLER - to filter certain elements from the list
even = list(filter(is_even,numbers))
print(even)

#filter operation using lambda
odd = list(filter(lambda n:n%2!=0,numbers))
print(odd)

#MAP -- Updating the values
update = list(map(lambda n:n*2,odd))
print(update)

#Reduce
sum = reduce(lambda a,b:a+b,numbers)
print(sum)

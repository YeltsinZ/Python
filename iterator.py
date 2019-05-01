# ITERATOR - will print only one value at time
numbers = [3,5,6,7,9]
val = iter(numbers)
#_next_() is a inbuild function which is part of iterator
print(val.__next__()) # prints the first value
print(val.__next__()) # prints the second value
# to create a own iterator
class TopTen:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if (self.num <= n):
            val = self.num
            self.num+=1
            return val
        else:
            raise StopIteration
print("Enter the range of numbers to be printed")
global n
n = int(input())
values = TopTen()
for i in values:
    print(i)

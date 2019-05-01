def topten():
    #converting a function to a generator
    n = 1
    while n <= 10:
        sq = n*n
        yield sq
        n += 1

values = topten()
for i in values:
    print(i)
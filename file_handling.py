
f = open('demo','r')

print(f.readline(),end="")
print(f.readline())

f1 = open('demo_2','w')
f1.write("This is a write file of File Handling",)
f1.write("Holy shit..!!! I'm appending the file",)

for data in f:
    print(data)
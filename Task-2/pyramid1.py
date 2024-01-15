pyramid1 = int(input("enter the no of rows"))
space = pyramid1

for i in range(0,pyramid1+1):
    for j in range(0,space):
        print(end=' ')
    space = space-1
    for k in range(0,i+1):
        print(k,end=' ')
    print()

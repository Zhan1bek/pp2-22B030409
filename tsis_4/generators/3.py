def printValues(n):
    for i in range(0, n):
        if(i % 4 == 0 and i % 3 == 0):
             x.append(i)
    print(x)

x = []
n = int(input())
printValues(n)
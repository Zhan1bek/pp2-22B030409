def printValues(n):
	l = list()
	for i in range(1,n):
		l.append(i**2)
	print(l)

n = int(input())
printValues(n)
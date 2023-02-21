def printValues(a, b):
	l = list()
	for i in range(a, b):
		l.append(i**2)
	print(l)

a = int(input())
b = int(input())
printValues(a, b)
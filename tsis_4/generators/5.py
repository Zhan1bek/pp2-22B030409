def odd(n):
    while n>=0:
        yield n
        n-=1
for i in odd(10):
    print(i)
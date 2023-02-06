def myfunc(n):
    return lambda b: b * n


mydoubler = myfunc(2)

print(mydoubler(11))

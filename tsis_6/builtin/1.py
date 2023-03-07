def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print(multiply((1, 2, 3, 4, 5)))
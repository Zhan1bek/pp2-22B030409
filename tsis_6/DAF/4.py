def countLines(filename):
    file = open(filename, 'r')
    count = 0
    for line in file:
        count += 1
    return count
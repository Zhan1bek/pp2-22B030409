def generateFiles():
    for char in ascii_uppercase:
        file = open(f'./files/{char}.txt', 'x')
        file.close()
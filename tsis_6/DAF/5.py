def writeToFile(filename, new_list):
    file = open(filename, 'a')
    file.write(str(new_list))
    file.close()

    file = open(filename , 'r')
    print(file.read())
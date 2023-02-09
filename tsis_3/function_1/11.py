def histogram( list ):
    for i in list:
        output = ''
        j = int(i)
        while( j > 0 ):
          output += '*'
          j = j - 1
        print(output)


list = input().split()
histogram(list)
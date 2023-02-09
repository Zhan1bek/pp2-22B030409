def solve(numheads, numlegs):
     for i in range(numheads + 1):
         j = numheads - i
         if i * 2 + j * 4 == numlegs:
             return(i, j)


h = 35
l = 94
print(solve(h, l))
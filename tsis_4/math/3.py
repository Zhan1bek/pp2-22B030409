import math

num_sides = int(input())
length = int(input())

area = (num_sides * length**2) / (4 * math.tan(math.pi / num_sides))
print(int(area))
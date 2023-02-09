def unique(list):
  x = []
  for i in list:
    if i not in x:
      x.append(i)
  return x


list = input().split()
print(unique(list))
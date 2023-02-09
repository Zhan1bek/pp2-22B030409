def prime_filter(number):
   for i in range(2, int(number)):
      if int(number) % i == 0:
         return False
   return True
number = input().split()
for i in list(number):
   if prime_filter(i):
      print(i, end=" ")
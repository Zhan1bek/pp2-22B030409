import random

random_number = random.randint(1, 20)
print("Hello! What is your name?")
user_name = input()
print("Well, " + user_name, ", I am thinking of a number between 1 and 20.")
flag = 1
print(random_number)
while flag == 1:
    count = 1
    number = input()
    if int(number) < int(random_number):
        count += 1
        print("""Your guess is too low.
Take a guess.""")
    elif int(number) > int(random_number):
        count += 1
        print("""Your guess is too big.
Take a guess.""")
    elif int(number) == int(random_number):
        print("Good job," +user_name, "! You guessed my number in " + str(count),"guesses!")
        flag = 0

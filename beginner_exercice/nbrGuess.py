import random
import math

lower = int(input("What number are you starting from?"))
upper = int(input("up to?"))

numbers = random.randint(lower, upper)
print(numbers)

print("\n\tYou now have", round(math.log(upper - lower +1, 2)),
    "chances to find the right number\n")

count = 0

while count < math.log(upper - lower + 1, 2):
    count += 1
    guess = int(input("What is the number?"))

    if guess == numbers:
        print("Congratulations, you found the right number!")

        break

    elif guess > numbers:
        print("too high")
    elif guess < numbers:
        print("too low")

    if count >= math.log(upper - lower +1, 2):
        print("\n\tfailure, The number was", numbers)
        print("\n\ttry your luck again!\n\t")

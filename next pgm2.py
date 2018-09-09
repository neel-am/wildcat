import random

fruits = ("apples", "mangos", "grapes", "lychee", "banana")
items = random.choice(fruits)
print()

game = input("Would you like to have some fun playing?: [y/n]")
if game == "n":
    print("its okay no problem Bye Bye !")
    exit()

if game == "y":
    print("Please guess your option:")

display = []
display.extend(items)

for i in range(len(display)):
    display[i] = "____"
print(items)
print(' '.join(display))
print()

count = 0

while count < 10:
    guess = input("Please guess a letter:")
    guess = guess.lower()

    print(guess)
    print(count)
    count = count + 1


    for i in range(len(items)):
        if items[i] == guess:
            display[i] = guess

            print(' '.join(display))
            print()


print("GOOD JOB!")







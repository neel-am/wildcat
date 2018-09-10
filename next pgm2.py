import random

fruits = ("apples", "mangos", "grapes", "lychee", "banana",)
items = random.choice(fruits)
print()

game = input("Would you like to have some fun playing?: [y/n]")
if game == "n":
    print("its okay no problem Bye Bye !")
    exit()

if game == "y":
    print("Please guess your option:")
correct = []
incorrect = []
display = []
display.extend(items)

for i in range(len(display)):
    display[i] = "____"


print(items)
print(' '.join(display))
print()

count = 1

while count < 10:
    guess = input("Please guess a letter:")

    if guess in correct or guess in incorrect:
        print("you have already guessed that letter guess again:")
    elif len(guess) == 1:
        print("please enter again")
    else:
        break
    if guess in items:
        correct.append(guess)
    else:
        incorrect.append(guess)

    count = count + 1
    guess = guess.lower()

    print(guess)
    print(count)


    for i in range(0, 6):
        if items[i] == guess:
            display[i] = guess

            print(' '.join(display))
            print()



print("Bye bye")









import random

items = ("jeeps", "honda", "carss", "bennz")
random.choice(items)
items = list(items[2])
print()

uname = input("hello, What is your name?:")

print("hello", uname + ".", )

answer = input("would you like to play game? : [y/n]")
if answer == "n":
    print("bye bye")
    exit()

if answer == "y":
    print("guess a choice:")

display = []
display.extend(items)

for i in range(len(display)):
    display[i] = "____"
print(items)
print(' '.join(display))
print()

count = 0

while count < len(items):
     guess = input("please guess a letter:")
     guess = guess.lower()
     print(guess)
     print(count)

     for i in range(len(items)):

          if items[i] == guess:

              display[i] = guess
              count = count + 1


     print(' '.join(display))
     print()


print("well done")



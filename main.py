import random

b = random.randint(-100,100)

found = False
while found == False:

  a = int(input("Guess the right number!: "))

  if a == b:

    found = True
    print("You Got It!")
  elif a < b:
    print(str(a), "Less than it")
  elif a > b:
    print(str(a),"More than it")
  else:
    print("Not a number")

  #I got a lot of it on my own but couldn't figure out how to get the if, else statements to work so I had to copy your work
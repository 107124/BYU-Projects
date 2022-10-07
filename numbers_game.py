import random
import os

while True:
  #clearing the console every time the user repeats the game
  os.system("clear")
  magic_number = random.randint(1, 100)

  print("\nWelcome to the game!")
  print(magic_number)

  count = 0
  guess = -1
  while guess != magic_number:
    try:
      guess = int(input("Guess between 1 and 100: "))
      print(guess)
      if guess > magic_number:
        print("Sorry, that guess was too high.")
      elif guess < magic_number:
        print("Sorry, that guess was too low.")
    except:
      print("Oops! You must enter a whole number.")

    count = count + 1

  print("You did it!")
  print(f"It took you {count} guesses.")
  again = input("Do you want to play the game again? ")
  if again.lower() != "yes":
    break



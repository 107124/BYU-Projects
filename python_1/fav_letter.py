"""
File: L08_Team_Activity.py
Authors: Hyrum Leishman, Jacob Buffington, Kent Taylor

Purpose: Sort through letters in a sentance by an input from the user.
"""
underscore = False

word_letters = []
word = ("In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost.")
for i in word:
  i = i.lower()
  word_letters.append(i)

stop = False
while not stop:
  choice = input("Do you want to change by LETTER or NUMBER? ")
  change = input("Do you want to HIDE or CAPITALIZE? ")
  if change.lower() == "hide":
    underscore = True
  else:
    underscore = False


  if choice.lower() == "number":
    number = int(input("Enter your favorite number: "))
    print()

    for i, letter in enumerate(word_letters):
      if i % number == 0:
        if underscore:
          print("_", end="")
        else:
          print(letter.upper(), end="")
      else:
        print(letter, end="")

  elif choice.lower() == "letter":
    fav_lettter = input("Enter your favorite letter: ")
    print()

    for i in word_letters:
      if i == fav_lettter.lower():
        if underscore:
          print("_", end="")
        else:
          print(fav_lettter.upper(), end="")
      else:
        print(i, end="")
  play_again = input("\n\nDo you want to play again?: ")
  print()
  if play_again.lower() == "no":
    stop = True
print("Goodbye")
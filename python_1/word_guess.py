def check_guess(guesses=[], user_guess="", secret_word="", correct_guesses=[]):
   if len(guesses[-1]) > 1:
       for char in guesses[-1]:
            guesses.append(char)

   correct_num = len(correct_guesses)
   print("Hint:  ", end="")
   for letter in secret_word:
       if letter in guesses:
           print(f" {letter.upper()} ", end="")
       else:
           print(" _ ", end="")

   print()
   combined_guesses = "".join(guesses)
   print(f"\nYour guesses so far: {[lett for lett in guesses]} ")

   for guess in combined_guesses:
       if guess in secret_word:
           if guess not in correct_guesses:
               correct_guesses.append(guess)
               if len(correct_guesses) == len(secret_word):
                   return True



secret_word = "beans"
guesses = []
user_guess = ""
correct_guesses = []
win = False
guess_num = 0

print("Hint:  ", end="")
for letter in secret_word:
    if letter in guesses:
        print(f" {letter.upper()} ", end="")
    else:
        print(" _ ", end="")

while True:

    if win:
        print(f"You won! The secret word was {secret_word}")
        break

    user_guess = input("\nGuess a letter: ").lower()
    guess_num += 1
    if len(user_guess) > len(secret_word):
        print("I'm sorry, you must guess something the same amount of letters as your hint. Try again!")
    else:
        if user_guess not in secret_word:
            print(f"Sorry, {user_guess} is not in the secret word. Try again!")

    guesses.append(user_guess)
    print(f"Number of guesses: {guess_num}")
    win = check_guess(guesses, user_guess, secret_word, correct_guesses)


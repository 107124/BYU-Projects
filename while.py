while True:
    number = int(input("Please type a positive number: "))

    if number >= 0:
        break
    else:
        print("Sorry, that is a negative number Please try again!")


print(f"The number is: {number}")


while True:
    answer = input("May I have a piece of candy?\n").lower()

    if answer == "yes":
        break
    elif answer == "no":
        pass
    else:
        print("Wait, i asked you a 'yes' or 'no' question!")


print("Thank you.")
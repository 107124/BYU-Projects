num_one = int(input("What is the first number?\n"))
num_two = int(input("What is the second number?\n"))

if num_one > num_two:
    print("The first number is greater.")
else:
    print("The first number is not greater.")

if num_one == num_two:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

if num_two > num_one:
    print("The second number is greater.")
else:
    print("The second number is not greater.")

my_fav_animal = "dolphin"
user_fav_animal = input("What is your favorite animal?\n").lower()

if user_fav_animal == my_fav_animal:
    print(f"Hey! We both have the same favorite animal of a {my_fav_animal}!")
else:
    print(f"A {user_fav_animal} is not my favorite animal.")
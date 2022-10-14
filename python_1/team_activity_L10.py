""""
File: L09_Team_Activity.py
Authors: Kent Taylor, Jacob Buffington, Hyrum Leishman, KC Williamson

Purpose: Compare numbers in a list.
"""

# Compute the sum, or total, of the numbers in the list.

# Compute the average of the numbers in the list.

# Find the maximum, or largest, number in the list.

numbers = []

def num_average(numbers):
    length = len(numbers)
    total = 0
    for num in numbers:
        total += num

    average = total / length
    return average

def lowest_positive(numbers):
  lowest = max(numbers)
  for i in numbers:
    if i > 0:
      if i < lowest:
        lowest = i
  if lowest > 0:
    return lowest
  else:
    return


print("Enter a list of numbers, type 0 when finished.")

number = ""
while number != 0:
  number = int(input("Enter a number: "))
  if number != 0:
    numbers.append(number)

if len(numbers) != 0:
  print(f"The average of the numbers is: {num_average(numbers)}")

  print(f"The max number is {max(numbers)}")

  print(f"The sum of the numbers is: {sum(numbers)}")

  print(f"The lowest positive number is {lowest_positive(numbers)}")

  numbers.sort()
  print(numbers)
else:
  print("There is nothing in the list.")
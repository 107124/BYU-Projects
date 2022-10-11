'''

- I added a dictionary of desserts and their prices.
- I used a list comprehension to display the dessert menu to the user 
  with its prices.
- I added a user-input-validator to make sure the user enters a dessert listed on the menu, if not it will just keep asking and letting the user know what they entered was not on the menu. Also forced the user input to be lowercased so as long as their spelling is correct we will take it!
'''

desserts = {
    "cake": 6.99,
    "donuts": 1.99,
    "ice cream": 2.99
}


# The price of a child's meal (floating point)
child_meal = float(input("How much was the child's meal?\n"))
# The price of an adult's meal (floating point)
adult_meal = float(input("How much was the adults's meal?\n"))


# The number of children (integer)
num_child = int(input("How many children were there?\n"))
# The number of adults (integer)
num_adult = int(input("How many adults were there?\n"))


# have them chose a dessert to share:
dessert_display = [print(f"{dessert}: ${price}") for dessert, price in desserts.items()]


while True:
    dessert_choice = input("Which dessert would you like?\n").lower()


    dessert_total = 0


    if dessert_choice == "cake":
        print("Cake it is!")
        dessert_total = desserts["cake"]
        break
    elif dessert_choice == "donuts":
        print("I hope you're okay with fresh donuts...")
        dessert_total = desserts["donuts"]
        break
    elif dessert_choice == "ice cream":
        print("I hope that's not too cold for you!")
        dessert_total = desserts["ice cream"]
        break
    else:
        print(f"I'm sorry, {dessert_choice} is not on our menu.")



print(f"Dessert charge: ${dessert_total}")



# The sales tax rate (floating point)
sales_tax = float(input("What's the current sales tax?\n"))


# Determine the meal's subtotal (before adding sales tax) by multiplying the number of children by the price of their meal,
# and multiplying the number of adults by the price of their meal and adding those two values together.
children_meal_total = child_meal * num_child
adult_meal_total = adult_meal * num_adult
group_subtotal = children_meal_total + adult_meal_total + dessert_total
# Display the subtotal.
print(f"Subtotal: ${group_subtotal}")


# Compute and display the sales tax, by multiplying the subtotal by the sales tax rate divided by 100.
tax_total = (sales_tax * group_subtotal) / 100
# Compute and display the total price of the meal by adding the subtotal and the sales tax.
group_total = group_subtotal + tax_total


print(f"Sales Tax: ${round(tax_total, 2)}")
print(f"Total: ${round(group_total, 2)}")


# Finally:


# Ask the user for the the payment amount (floating point)
payment = float(input("How much money are you giving me?\n"))
# Compute and display the change.
change = payment - group_total
print(f"Your change is ${round(change, 2)}")
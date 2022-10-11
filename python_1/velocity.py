from cmath import pi
from re import sub

childs_meal = float(input("Childs meal: "))
adults_meal = float(input("Adults meal: "))
total_children = int(input('Total children: '))
total_adults = int(input('Total adults: '))
sales_tax_rate = int(input('What is the sales tax: '))
Payment_amount = int(input('What is the payment amount: '))

print(' ')
print(str(f"What is the price of a child's meal? ${childs_meal}" ))
print(str(f"What is the price of an adult's meal? ${adults_meal}" ))
print(str(f"How many children are there? {total_children}" ))
print(str(f"How many adults are there? {total_adults}" ))
print(str(f"What is the sales tax rate? {sales_tax_rate} " ))
print(' ')

subtotal = childs_meal * 2 + adults_meal
# subtotal = childs_meal * 4 + adults_meal * 2
# pi_0 = subtotal
print(f"Subtotal: ${subtotal}")
Sales_tax = subtotal * sales_tax_rate / 100

pi = Sales_tax
print(f"Sales tax: ${pi:.2f}")
Total = subtotal
Sub_total = subtotal + Sales_tax
pi_2 = Sub_total
print(f"Total: ${pi_2:.2f}")
print(' ')

print(f"What is the payment amount: ${Payment_amount} ")
Change = Payment_amount - Total - pi
pi = Change
print(f"Change: ${pi:.2f}")











# print(f"the number is {8}.")
# Extra creativity:
# I imported time to have a more legible user interface. I also added a try catch clause for the users price input to make sure it's
# a number, and loops back until the user gives a number.

from time import sleep

def show_cart(cart, item_prices):
    sleep(1)
    print("\nHere are your cart items: ")
    sleep(2)
    inc = 0
    for item in cart:
        print(f"{inc + 1}: {item.title()} - ${round(item_prices[inc], 2)}")
        inc += 1
        sleep(1)
    return



cart = []
item_prices = []

while True:
    menu = ["\n1: Add new item ", "2: Display your shopping cart ", "3: Remove item ", "4: Compute total ", "5: Quit "]
    [print(item) for item in menu]
    menu_ui = int(input("What would you like to do? "))

    if menu_ui == 1:
        item_to_add = input("What item would you like to add? ")
        while True:
            try:
                price_to_add = float(input(f"What's the price for {item_to_add}? "))
                break
            except ValueError as err:
                print(f"You must enter a number, {err} was given.")

        cart.append(item_to_add)
        item_prices.append(price_to_add)
        print(f"{item_to_add.title()} - ${price_to_add} successfully added.") # eventually made this a try catch

    elif menu_ui == 2:
        show_cart(cart, item_prices)
    elif menu_ui == 3:
        show_cart(cart, item_prices)
        while True:
            remove_input = int(input("What item (#) would you like to remove from your cart? "))
            try:
                cart[remove_input - 1]
                removed = cart.pop(remove_input - 1)
                item_prices.pop(remove_input - 1)
                print(f"Looking for your {removed}")
                sleep(1)
                print(f"Removed {removed} successfully!")
                sleep(1)
                break
            except:
                sleep(1)
                print("Item not found, try again.")
                sleep(1)
    elif menu_ui == 4:
        cart_total = sum(item_prices)
        sleep(1)
        print(f"Here is your cart total so far: ${round(cart_total, 2)}")
        sleep(2)
    elif menu_ui == 5:
        break



sleep(2)
print("Have a nice day!")
sleep(1)


from time import sleep

cart = []

while True:
    menu = ["\n1: Add new item ", "2: Display your shopping cart ", "3: Quit "]
    [print(item) for item in menu]
    menu_ui = int(input("What would you like to do? "))

    if menu_ui == 1:
        item_to_add = input("What item would you like to add? ")
        cart.append(item_to_add)
        print(f"{item_to_add.title()} successfully added.") # eventually make this a try catch
    elif menu_ui == 2:
        sleep(1)
        print("\nHere are your cart items: ")
        sleep(2)
        for item in cart:
            print(item.title())
            sleep(1)
    elif menu_ui == 3:
        break


print("Have a nice day!")


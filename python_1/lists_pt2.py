items = ["juice", "milk", "cereal", "applesauce", "toy", "tooth brush", "razor", "dog food"]

for item in items:
    print(f"Item: {item}")


for i in range(0, 8):
    print(f"{i}: {items[i]}")


change = int(input("What item in your cart would you like to change? "))
new_item = input("Name the new item: ")

for i in range(0, 8):
    if i == change:
        print(f"{i}: {new_item}")
    else:
        print(f"{i}: {items[i]}")
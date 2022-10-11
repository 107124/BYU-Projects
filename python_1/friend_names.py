friends = []

while True:
    friend = input("Enter a friends name: ").lower()
    if friend == "end":
        break
    
    friends.append(friend)


for name in friends:
    print(name)
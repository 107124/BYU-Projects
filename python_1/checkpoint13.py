def display_regular(string):
    return string


def display_uppercase(string):
    return string.upper()


def display_lowercase(string):
    return string.lower()


message = input("What is your message? ")

print(display_regular(message))
print(display_uppercase(message))
print(display_lowercase(message))
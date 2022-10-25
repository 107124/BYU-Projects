import math

def compute_area(shape, meters_one, meters_two=0):

    if shape == "square":
        square_area = meters_one ** 2
        return(square_area)

    elif shape == "circle":
        circle_area = math.pi * radius ** 2
        return(circle_area)

    elif shape == "rectangle":
        rectangle_area = meters_one * meters_two
        return(rectangle_area)


while True:
    shape = input("What shape do you want to calculate? ").lower()
    if shape == "quit":
        break
    elif shape == "circle":
        radius = float(input("What is the radius of the circle? "))
        print(compute_area(shape, radius))

    elif shape == "square":
        meters = float(input("How long is one side length of the square? "))
        print(compute_area(shape, meters))

    elif shape == "rectangle":
        meters_one = float(input("How long is one side length of the rectangle? "))
        meters_two = float(input("How long is the other side length of the rectangle? "))
        print(compute_area(shape, meters_one, meters_two))

    else:
        print("I'm sorry we don't recognize that shape, try again.")





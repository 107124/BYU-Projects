people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest = 200

for person in people:
    person = person.strip()
    person = person.split()
    print(person)

    if int(person[1]) < youngest:
        youngest = int(person[1])
        youngest_person = person

print(youngest)
print(f"The youngest person is {youngest_person}")


with open("hr_system.txt") as file:
    for item in file:
        person_list = item.split()
        name = person_list[0]
        person_id = person_list[1]
        title = person_list[2]
        salary = float(person_list[3])
        bi_monthly_salary = salary / 24
        bonus = 1000

        if title == "Engineer":
            print(f"{name}\t(ID: {person_id}), {title} - ${(bi_monthly_salary + bonus):.2f}")
        else:
            print(f"{name}\t(ID: {person_id}), {title} - ${(bi_monthly_salary):.2f}")


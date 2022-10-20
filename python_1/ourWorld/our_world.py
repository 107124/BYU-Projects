year_list = []

group_list = []
av_life_list = []

with open("life-expectancy.csv") as facts:
    # search = int(input("Enter a year of interest: "))
    for fact in facts:
        line = fact.split("\n")
        line = line[0].split(",")
        country, country_code, year, life_ex = line
        # year_list.append(year)
        country = line[0]
        country_code = line[1]
        year = line[2]
        life_ex = line[3]
        group = (country, country_code, year, life_ex)
        group_list.append(group)
        year_list.append(year)
        print(line)

    for pair in group_list:
        av_life = pair[3]
        av_life_list.append(av_life)
        av_life_list.sort()

    biggest_av = av_life_list[-2]
    smallest_av = av_life_list[0]

    print(f"Smallest Average: {smallest_av}")
    print(f"Biggest Average: {biggest_av}")
    # print(year_list)
    # print(av_life_list)

    # pair = zip(year_list, av_life_list[0:-1])
    # print(list(pair))
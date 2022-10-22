from xml.etree.ElementTree import QName


year_list = []

group_list = []
av_life_list = []

min = 200
max = -1
min_av = ""
max_av = ""
life_year_list = []

new_max = -1
new_min = 200
search_max = ""
search_min = ""


with open("life-expectancy.csv") as facts:
    search = int(input("Enter a year of interest: "))
    for fact in facts:
        try:
            line = fact.strip()
            line = line.split(",")

            if float(line[3]) < min:
                min = float(line[3])
                min_av = line

            elif float(line[3]) > max:
                max = float(line[3])
                max_av = line

            if int(line[2]) == search:
                life_year_list.append(float(line[3]))

                if float(line[3]) < new_min:
                    new_min = float(line[3])
                    search_min = line

                elif float(line[3]) > new_max:
                    new_max = float(line[3])
                    search_max = line

        except:
            pass


    print(f"\nOverall:\nmin: ", min)
    print(f"Min line is: ", min_av)
    print(f"\nmax: ", max)
    print(f"max line is: ", max_av)
    average = sum(life_year_list) / len(life_year_list)
    print(f"\n\nThe average world life expectancy for the year {search} is : {average}")
    print(f"\n{search_min[0].title()} has the lowest life expectancy average of {new_min} for the year {search}")
    print(f"\n{search_max[0].title()} has the highest life expectancy average of {new_max} for the year {search}\n")

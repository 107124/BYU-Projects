from time import sleep

# This is to update my stats as well as display it for the user.
def show_stats(**stats):
        total = 0
        stat_total = sum([value for stat, value in stats.items()])
        sleep(1)
        print()
        [print(f"{stat.title()}: {points}") for stat, points in stats.items()]
        print()
        sleep(1)

        return(stat_total)


# This is my first scenario for the assignment.
def alarm():
    # These refer to the dictionary i made at the end of this file, defaulting the stats at 100.
    alert = stats["alert"]
    health = stats["health"]
    strength = stats["strength"]

    # i'm using user-input-validation to make sure they don't choose something that's NOT a choice.
    while True:
        print('You wake up to your alarm "beep beep beep beep..."')
        alarm = input("What do you do?\nSNOOZE or GET UP: ").lower()

        if alarm == "snooze":
            # They lose points for snoozing
            alert -= 10
            health -= 10
            strength -= 5

            sleep(1)
            print("\nYou lost some health stats")

            stat_total = show_stats(alert=alert, health=health, strength=strength)

            # If they snooze too many times they become a zombie and forces them out of bed.
            if stat_total <= 175:
                print("** OH NO! You're now a walking zombie **")
                show_stats(alert=alert, health=health, strength=strength)
                return(alert, health, strength)


        # This will output different 
        elif alarm == "get up":
            if stat_total == 300:
                print("\nYou get up feeling 100%!\n")
            elif stat_total > 250:
                print("\nYou get up feeling mostly rested... But you could have got up the first time\n")
            else:
                print('\n"You finally get up, but not feeling so great after all the snoozing.')

            show_stats(alert=alert, health=health, strength=strength)
            return(alert, health, strength)
            # break
        else:
            print(f"I'm sorry, {alarm} is not an option.")


def breakfast_time(stat_update):
    alert, health, strength = stat_update
    while True:
        print('"It\'s time for breakfast!" Your mom calls. You come downstairs to the kitchen.\nshe has lovingly made you eggs and sausage for your own well being and good strength.')
        breakfast = input("What sounds good to you?\nTAKE IT or CANDY: ").lower()

        if breakfast == "candy":
            alert -= 3
            health -= 15
            strength -= 15

            sleep(1)
            print("\nOUCH! That took a hit on your overall health.")

            show_stats(alert=alert, health=health, strength=strength)
            break
        elif breakfast == "take it":
            alert += 10
            health += 15
            strength += 15

            sleep(1)
            print("\nBoth delicious AND great for your health!")

            show_stats(alert=alert, health=health, strength=strength)
            break
        else:
            print(f"{breakfast} isn't a choice, try again!")


stats = {
    "alert": 100,
    "health": 100,
    "strength": 100
}



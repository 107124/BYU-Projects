from time import sleep

# This is to update my stats as well as display it for the user.
def show_stats(**stats):
        total = 0
        stat_total = sum([value for stat, value in stats.items()])
        sleep(1)
        print()
        [print(f"{stat.title()}: {points}") for stat, points in stats.items()]
        print()
        sleep(3)

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

            sleep(3)
            print("\nYou lost some health stats")

            stat_total = show_stats(alert=alert, health=health, strength=strength)

            # If they snooze too many times they become a zombie and forces them out of bed.
            if stat_total <= 175:
                print("** OH NO! You're now a walking zombie **")
                show_stats(alert=alert, health=health, strength=strength)
                breakfast_time(alert, health, strength)
                break


        # This will output different
        elif alarm == "get up":
            stat_total = show_stats(alert=alert, health=health, strength=strength)

            if stat_total == 300:
                print("\nYou get up feeling 100%!\n")
            elif stat_total > 250:
                print("\nYou get up feeling mostly rested... But you could have got up the first time\n")
            else:
                print('\n"You finally get up, but not feeling so great after all the snoozing.')

            breakfast_time(alert, health, strength)
            break
        else:
            print(f"I'm sorry, {alarm} is not an option.")


def breakfast_time(*stat_update):
    alert, health, strength = stat_update
    while True:
        print('"It\'s time for breakfast!" Your mom calls. You come downstairs to the kitchen.\nshe has lovingly made you eggs and sausage for your own well being and good strength.')
        breakfast = input("What sounds good to you?\nTAKE IT or CANDY: ").lower()

        if breakfast == "candy":
            alert -= 3
            health -= 15
            strength -= 15

            sleep(3)
            print("\nOUCH! That took a hit on your overall health.")

            show_stats(alert=alert, health=health, strength=strength)
            final_choice("candy", (alert, health, strength))
            break
        elif breakfast == "take it":
            alert += 10
            health += 15
            strength += 15

            sleep(3)
            print("\nBoth delicious AND great for your health!")

            show_stats(alert=alert, health=health, strength=strength)
            final_choice("take it", (alert, health, strength))
            break
        else:
            print(f"{breakfast} isn't a choice, try again!")


def final_choice(next_choice, stat_update):
    alert, health, strength = stat_update
    while True:
        if next_choice == "candy":
            print("""
            Your health has taken a huge toll due to a bad breakfast choice.
            It's difficult for you to breathe and make simple decisions.
            """)
            sleep(2)
            print("""
            You walk to school and come to a crosswalk of a busy road.
            But you can't think straight on what to do next as the pedestrian sign
            starts to blink red.
            """)
            cross_walk = input("Do you CROSS FAST or TAKE FRIEND across with you so that traffic is more likely to stop if they see more people? ").lower()

            if cross_walk == "cross fast":
                print("You run sooooo fast! The sugar in your veins makes you faster than you ever thought you could go before!")
                sleep(3)
                print("However.... a motorcyclist coming up ALSO had candy for breakfast and is trying to beat you.")
                sleep(3)
                print("then...")
                sleep(3)
                show_stats(alert=0, health=0, strength=0)
                break
            elif cross_walk == "take friend":
                print("Your friend is confused on why you're trying to force them to cross a busy road")
                sleep(3)
                print("But the cars next to you are not quite finished with their red light. So you convince them that this is somehow a good idea.")
                sleep(3)
                print("The delay from pulling your friend along cost you enough time to break a friendship forever...")
                sleep(3)
                print("oh.")
                sleep(2)
                print("... and you also lost your arm.")
                sleep(3)
                show_stats(alert=0, health=0, strength=0)
                break
            else:
                sleep(2)
                print(f"I'm sorry, {cross_walk} isn't a choice. Try again.")
                sleep(2)


        elif next_choice == "take it":
            print("Your body is full of good food, your health and mind is at a pretty good place!")
            sleep(2)
            print("With your body healthy and spirituality in good standing, you hear a still small voice whisper: ")
            sleep(2)
            print("Hand the homeless man your school lunch.")
            sleep(2)
            serve = input("Do you SERVE or IGNORE because you need that lunch for school-brain-power for your test later? ").lower()
            sleep(2)


            if serve == "serve":
                print("You take out your lunch sack that mom made for you, and without thinking twice, you hand it to the poor man.")
                sleep(4)
                print("At first he refuses, but you'd rather listen to the spirit and hand it over to him and walk away.")
                sleep(4)
                print("The poor man was asking Heavenly Father for money that day so he can feed himself and his child that was hiding behind the trash cans.")
                sleep(4)
                print("He didn't realize God would send you instead of money, and now their belly's are full and so is your spiritual and physical health.")
                sleep(4)
                print("Heavenly Father helps your mind with your test later that day for following His prompting.")
                sleep(4)
                show_stats(alert=alert, health=health, strength=strength)

                break
            elif serve == "ignore":
                print("You chose to ignore this prompting...")
                sleep(2)
                print("Later at school, a bully takes your lunch.")
                sleep(3)
                print("Now neither you, nor the homeless man who also has a hungry child, get to eat that day.")
                sleep(4)
                show_stats(alert=alert, health=health, strength=strength)

                break
            else:
                sleep(2)
                print(f"I'm sorry, {serve} isn't a choice. Try again.")
                sleep(2)

stats = {
    "alert": 100,
    "health": 100,
    "strength": 100
}

# This stores and runs the alarm function and set up choices in functions.py:
stat_update = alarm()
# This sends the updated stats to breakfast_time to reduce repeated code.
# next_choice will be holding the value of the final decision of breakfast_time and will
# determain how the third sceniaro plays out:

# Prints after all the functions return.
print("GAME OVER\n\n")


